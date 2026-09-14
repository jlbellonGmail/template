# T04 — Integridad de sincronización y cierre transversal

Estado: READY_FOR_PR · Versión: v2.0.0 · Tipo: Maintenance / Transversal · SDD: STANDARD · PR: pendiente · Merge: pendiente

## Objetivo

Eliminar inconsistencias entre ROADMAP, STATUS, runs, SUMMARY, Git, PR/merge,
CI y worktrees, diferenciando fases Fxx de intervenciones Txx.

## Resultado

Se agrega un checker determinista global, soporte de lifecycle Maintenance/Txx,
registro comprobable de T01–T03 y cleanup seguro con `git worktree prune`.

## Cambios principales

- T02 y T03 quedan registrados con sus PRs reales; T01 conserva su estado real.
- El checker detecta runs Txx huérfanos, registros sin evidencia, SUMMARY
  faltante, cierres sin PR/merge, contradicciones Fxx/STATUS y AUTO stale.
- El cleanup no fuerza contenido y clasifica worktree activo, residual vacío y
  residual con archivos.

## Validación

Pytest focalizado, checker global y escenarios de idempotencia ejecutados.

## Decisiones

Se evoluciona la infraestructura existente; no se crea base de datos ni se
implementan F13, F14, F15, F16 o F17.

## Incidencias

Los locks de CWD/handles Windows pueden dejar una carpeta física vacía; se
reportan sin borrar contenido. Una carpeta con archivos bloquea el cierre.

## Detalle

[spec](spec.md) · [plan](plan.md) · [tasks](tasks.md) · [audit](audit-1.md) ·
[QA](test-report-1.md) · [code review](code-review-1.md) · [decision](decision.md)
