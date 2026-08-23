# Plan: Operational readiness docs

Este plan describe el CÓMO para cada AC de `spec.md`. No repite el QUÉ
ni el POR QUÉ. Toda referencia `AC-N` remite a
`runs/05-operational-readiness-docs/spec.md`.

## 1. Arquitectura afectada

Feature puramente documental: no se toca código de producto (no existe),
ni `scripts/*.ps1`, ni `.github/workflows/*.yml`, ni `.agentic/*`, ni
`tests/*`. Se tocan exclusivamente:

- `AGENTS.md` (sección "Setup manual") — AC-1, AC-2, AC-3.
- `docs/tecnica/circuito-agentico.md` (nueva sección) — AC-4.
- `docs/tecnica/operational-readiness-docs.md` (nuevo) — AC-5.
- `docs/usuario/operational-readiness-docs.md` (nuevo) — AC-6.
- `runs/05-operational-readiness-docs/decision.md` (nuevo) — AC-7.
- `docs/tecnica/index.md` y `docs/usuario/index.md` (enlaces, vía
  `scripts/update-doc-indexes.ps1`, sin edición manual) — AC-8.

Explícitamente no se toca `.github/workflows/ci.yml` (pertenece a la
feature `04-ci-wiring-product-tests`, en curso en paralelo) ni
`scripts/local-feature-reconcile.ps1`/`scripts/ready-for-pr.ps1` (el
troubleshooting de EDR es un procedimiento manual, no un cambio de
comportamiento de esos scripts).

## 2. Componentes y contratos nuevos/modificados

### 2.1 `AGENTS.md` — checklist de branch protection (AC-1, AC-2, AC-3)

Agregar, como nuevo bullet dentro de "Setup manual (una sola vez, no
automatizable)" (después del bullet "Remoto GitHub" existente), el
siguiente contrato de contenido (texto real a redactar por
`builder-agent`, siguiendo este esqueleto):

```markdown
- **Branch protection de GitHub** (Settings → Branches → Branch
  protection rules, o vía `gh api`): configurar sobre la rama `develop`
  los cuatro requisitos que exige el circuito para que el único HITL
  (`AGENTS.md`, sección "Único HITL") sea efectivo: (a) exigir pull
  request antes de mergear, (b) exigir en verde el status check `test`
  (nombre del job actual de `.github/workflows/ci.yml`; si la feature
  `04-ci-wiring-product-tests` renombra o separa ese job, actualizar
  este comando con el nombre vigente antes de aplicarlo — verificar en
  la pestaña Actions de una PR reciente), (c) exigir al menos 1
  aprobación, (d) descartar (dismiss) aprobaciones obsoletas cuando hay
  un push nuevo a la PR. Requiere permisos de administrador sobre el
  repositorio y un remoto GitHub ya configurado (ver bullet "Remoto
  GitHub" arriba).

  Comando `gh api` (PowerShell; declarativo e idempotente — se puede
  re-ejecutar sin efectos duplicados; `{owner}`/`{repo}` los resuelve
  `gh` automáticamente desde el remoto del directorio actual, no hace
  falta reemplazarlos):

  ```powershell
  $branchProtection = @'
  {
    "required_status_checks": {
      "strict": true,
      "contexts": ["test"]
    },
    "enforce_admins": false,
    "required_pull_request_reviews": {
      "dismiss_stale_reviews": true,
      "required_approving_review_count": 1
    },
    "restrictions": null
  }
  '@

  # Validar el JSON localmente antes de enviarlo (no requiere credenciales):
  $branchProtection | ConvertFrom-Json | Out-Null

  $branchProtection | gh api `
    --method PUT `
    -H "Accept: application/vnd.github+json" `
    repos/{owner}/{repo}/branches/develop/protection `
    --input -
  ```

  Si la versión de la API en uso ya deprecó el campo `contexts` a favor
  de `checks`, reemplazar `"contexts": ["test"]` por
  `"checks": [{"context": "test"}]` dentro del mismo payload.

  Verificar lo aplicado (opcional, de solo lectura):

  ```powershell
  gh api repos/{owner}/{repo}/branches/develop/protection
  ```

  Alternativa manual (si no se confía en `gh api` o no está disponible):
  en GitHub, Settings → Branches → Add branch protection rule para
  `develop` → activar "Require a pull request before merging" con
  "Require approvals" = 1 y "Dismiss stale pull request approvals when
  new commits are pushed" → activar "Require status checks to pass
  before merging" y agregar el check `test` → Save.
```

`builder-agent` redacta el texto final en prosa/lista siguiendo el
patrón markdown ya usado por los bullets existentes de esa sección
(guion, negrita del título, referencias a `Settings → ...` como ya hace
el bullet "GitHub Pages"), preservando el contenido técnico exacto de
arriba (los 4 requisitos, el payload JSON, la nota de dependencia con la
feature `04`, la alternativa de UI).

### 2.2 `docs/tecnica/circuito-agentico.md` — troubleshooting EDR (AC-4)

Agregar una sección nueva al final del archivo (después de "Gate
post-HITL"):

```markdown
## Troubleshooting: EDR/antivirus agresivo bloquea el reconciliador local (Windows)

**Síntoma**: `ready-for-pr.ps1` lanza
`local-feature-reconcile.ps1 -StartBackground` como proceso de
PowerShell en segundo plano (`Start-Process ... -WindowStyle Hidden`,
ver `scripts/local-feature-reconcile.ps1`). En máquinas Windows con
software de seguridad (EDR/antivirus) agresivo, ese proceso de fondo
puede quedar bloqueado, terminado abruptamente o impedido de completar
sus operaciones de archivo sobre el worktree de la feature.

**Causa**: el EDR interfiere con el proceso PowerShell que corre en
background (comportamiento típico de heurísticas que tratan procesos
`powershell.exe` sin ventana visible como sospechosos), no con git, con
GitHub Actions ni con el estado remoto de `ROADMAP.md`.

**Alcance del problema**: es exclusivamente local a la máquina del
operador. No corrompe el estado de git, no afecta el CI de la PR, ni el
gate post-HITL, ni el cierre remoto de `ROADMAP.md` en `develop` (esos
tres corren en GitHub Actions, independientes de este proceso local). El
único efecto es que el worktree/rama local de la feature puede no
limpiarse automáticamente cuando corresponde.

**Solución**: reubicar el worktree en un path nuevo, forzando la
remoción del bloqueado:

```powershell
git worktree remove --force <path-del-worktree-bloqueado>
git worktree add <path-nuevo> <rama-de-la-feature>
```

`git worktree remove --force` descarta cualquier cambio sin commitear en
ese worktree — revisar `git status` ahí antes de forzar, si el worktree
sigue siendo accesible. El estado del reconciliador
(`<git-common-dir>/feature-reconcilers/`, ver
`Get-FeatureStateDir` en `scripts/feature-contract.ps1`) vive fuera de
cualquier worktree, así que no hace falta matar el proceso bloqueado
antes de remover el worktree. Después de recrear el worktree en el path
nuevo, se puede relanzar el reconciliador corriendo de nuevo
`scripts/ready-for-pr.ps1` (o directamente
`scripts/local-feature-reconcile.ps1 -Slug <slug> -StartBackground`)
desde ahí.
```

### 2.3 `docs/tecnica/operational-readiness-docs.md` (AC-5)

Documento técnico nuevo: decisiones de diseño de ambos puntos (por qué
`gh api` sobre UI manual, por qué solo `develop`, por qué
`enforce_admins: false`, por qué el troubleshooting vive en
`circuito-agentico.md` y no en un archivo nuevo, referencia explícita a
que esto cierra la "Recomendación operativa (no automatizada)" dejada
pendiente por `02-integridad-post-hitl-y-ready-for-pr`), y casos borde
cubiertos (permisos insuficientes, remoto ausente, status check
desactualizado, re-ejecución idempotente, lock file inerte, cambios sin
commitear al forzar el worktree).

### 2.4 `docs/usuario/operational-readiness-docs.md` (AC-6)

Documento de usuario nuevo: para quién es (quien administra el
repositorio GitHub del proyecto y quien opera el circuito localmente en
Windows), cuándo correr el checklist de branch protection (una vez, al
adoptar el circuito o cuando cambie el nombre del status check), y qué
hacer paso a paso si el reconciliador local queda bloqueado.

### 2.5 `runs/05-operational-readiness-docs/decision.md` (AC-7)

Documento canónico de decisiones demostrables: resume las decisiones de
2.1–2.4, sin afirmar aprobación de merge (esa aprobación es exclusiva
del HITL vía GitHub).

### 2.6 Índices de documentación (AC-8)

`builder-agent` ejecuta
`scripts/update-doc-indexes.ps1 05-operational-readiness-docs "Operational Readiness Docs"`
para agregar el enlace en ambos índices, sin edición manual de
`docs/tecnica/index.md`/`docs/usuario/index.md`.

## 3. Compatibilidad y migracion

No hay datos, artefactos ni ramas existentes que migrar: es
documentación nueva más una sección agregada a dos archivos `.md` ya
existentes (`AGENTS.md`, `docs/tecnica/circuito-agentico.md`). No cambia
el comportamiento de ningún script ni de ningún workflow existente. El
comando `gh api` documentado no se ejecuta como parte de esta feature ni
del circuito automatizado; su ejecución real contra el repositorio de
GitHub queda a criterio y momento del humano, igual que los demás
bullets de "Setup manual".

## 4. Dependencias

No se agrega ninguna dependencia nueva de build, backend, base de datos
o integración externa. `gh` (GitHub CLI) ya es una herramienta local
requerida por `AGENTS.md` (sección "Herramientas locales requeridas");
esta feature no agrega un requisito nuevo, solo documenta un uso
adicional de esa misma herramienta ya autorizada.

## 5. Impacto operacional

- El humano que administra el repositorio real en GitHub debe ejecutar
  manualmente, una sola vez (o cuando el nombre del status check
  cambie), el comando `gh api` documentado en AC-1/AC-2 — no lo ejecuta
  ningún agente ni script del circuito.
- Un operador en Windows que observe el síntoma de EDR descrito en AC-4
  sigue el procedimiento de `git worktree remove --force` +
  `git worktree add` documentado, sin intervención de ningún agente.
- Ningún script del circuito (`ready-for-pr.ps1`,
  `local-feature-reconcile.ps1`, `complete-approved-pr.ps1`,
  `close-feature.ps1`) cambia de comportamiento ni de interfaz.

## 6. Estrategia de tests

Esta feature no tiene lógica de servidor ni código ejecutable propio:
es documentación Markdown pura. No corresponde agregar tests de pytest
nuevos (no hay comportamiento de script para cubrir), consistente con
que el resto del repo no testea contenido textual de `AGENTS.md`/
`docs/tecnica/*.md` vía pytest.

La verificación es manual reproducible (`qa-agent` la ejecuta como parte
de correr `Assert-FeatureContract` más esta lista adicional):

- **AC-1, AC-2, AC-3**: abrir `AGENTS.md`, confirmar el bullet nuevo con
  los 4 requisitos, el comando `gh api` con el payload JSON completo, la
  nota de dependencia con la feature `04`, y la alternativa de UI.
  Validar sintácticamente el JSON embebido copiándolo y corriendo
  `$json | ConvertFrom-Json` en PowerShell (sin necesidad de credenciales
  de `gh` ni de un repositorio GitHub real) — cubre el caso borde de
  JSON inválido de `spec.md`.
- **AC-4**: abrir `docs/tecnica/circuito-agentico.md`, confirmar la
  sección de troubleshooting nueva con síntoma, causa, alcance y los dos
  comandos `git worktree` exactos — cubre el caso borde de lock file
  inerte y de cambios sin commitear al forzar el worktree.
- **AC-5, AC-6, AC-7, AC-8**: correr `pytest -v` completo (no debe
  romperse nada existente) y ejecutar
  `powershell -File .\scripts\update-doc-indexes.ps1 05-operational-readiness-docs "Operational Readiness Docs"`
  para confirmar que los índices quedan enlazados una sola vez.
