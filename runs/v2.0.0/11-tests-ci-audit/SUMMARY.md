# F06 — Tests, CI y `.audit`

Estado: listo para PR · Versión: v2.0.0 · Tipo: Feature
PR: pendiente · Merge: pendiente

## Objetivo

Base mínima profesional y determinística para tests, CI y auditoría global.

## Resultado

La suite existente se conserva por valor; se agregan invariantes de `.audit` y
se robustece el launcher Windows con argumentos `-File`. CI mantiene circuit,
product y reconciliación como responsabilidades separadas.

## Cambios principales

- `tests/test_audit_framework.py` verifica perfil, orden normativo,
  independencia y separación de evidencia.
- `local-feature-reconcile.ps1` evita `EncodedCommand` y selecciona el modo de
  proceso según el entorno.
- Product-tests continúa desacoplado del stack de producto.

## Validación

La suite focalizada, el contrato y los adaptadores pasan. Los tres timeouts
históricos se eliminaron separando el test del launcher del motor de lifecycle:
el job Windows mantiene ambos gates, pero los escenarios de cierre se ejecutan
en foreground para no depender del árbol de procesos del host.

## Decisiones

`.audit` no se fusiona con Reviewer ni se convierte en scoring agentic. No se
inicia ninguna fase posterior.

## Incidencias

Limitación ambiental local documentada; no evidencia un bug reproducible en
CI. Si CI Windows falla, el estado debe ser FAILED_SAFELY y no se fuerza el
merge.

## Detalle

[spec](spec.md) · [plan](plan.md) · [tasks](tasks.md) · [audit](audit-1.md) · [QA](test-report-1.md) · [code review](code-review-1.md) · [decision](decision.md)

## Paralelización futura

F07 requiere esta base y queda pendiente. F09 y F11 pueden evaluarse en
paralelo por dependencias reales cuando corresponda; F08 espera evidencia de
F07 y F10 espera la política relevante de seguridad si se afectan permisos o
confianza.
