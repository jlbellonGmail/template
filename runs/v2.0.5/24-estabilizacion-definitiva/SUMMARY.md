# 24-estabilizacion-definitiva

Estado: MERGED
Versión: v2.0.5
Tipo: Feature
SDD: FULL
PR: #117
Merge: 9f9b4655437ff97f4874eb3aee77f27f4e784828

## Objetivo

Estabilizar Template v2.0.5 corrigiendo STATUS-only, integridad de runs no canónicos y distribución/upgrades de consumidores.

## Resultado

Mergeada en `develop` mediante PR #117. El cierre oficial del ROADMAP quedó en `6090bd6090ea011849c7f0e7be0c58d5d804a4f1`. Pendiente tag/release v2.0.5 y validación post-release.

## Cambios principales

- Integridad sólo interpreta runs `Txx` bajo `runs/vX.Y.Z/`.
- Manifest compartido sube a schema 2 con `templateVersion` y `templateRepository`.
- Nuevo `scripts/upgrade-template-consumer.ps1` valida tags exactos, baseline/target, drift y trabajo pendiente.
- Documentación de adopción y STATUS actualizada.
- Regresiones para runs no canónicos y upgrade v2.0.4 -> v2.0.5.

## Validación

- Pruebas focalizadas: 25 passed.
- Upgrade: 4 passed.
- Suite completa: 281 passed en segunda corrida.
- Suite final post-evidencia: 280 passed + 1 fallo transitorio de permisos Git; test exacto reintentado y aprobado.
- Suite final post-follow-up: 282 passed.
- `check-status.ps1`: PASS.
- `check-integrity.ps1 -Version v2.0.5`: PASS.
- PR #117: CI `circuit-tests`, `product-tests`, `local-reconciler-tests` PASS sobre `c754d338dc400553c0d49b5ae2e8806e167ff369`.
- Merge PR #117: `9f9b4655437ff97f4874eb3aee77f27f4e784828`; cierre ROADMAP: `6090bd6090ea011849c7f0e7be0c58d5d804a4f1`.
- Suite completa post-merge y cierre: 282 passed.

## Decisiones

El upgrade copia únicamente `sharedPaths`; los consumidores anteriores sin `templateVersion` deben informar `-BaselineVersion`.

## Incidencias

Dos corridas completas tuvieron un fallo transitorio de permisos Git en `%TEMP%` al pushear a bare repos temporales; ambos tests exactos pasaron al reintentar. La corrida final posterior al follow-up pasó completa.

## Auditoría adicional pre-release

El guard de `develop` falló en el fallback de asociación de PRs porque se
pasaban `--arg` a `gh api`, que no soporta esa opción. La consulta ahora pasa
por `jq --arg`; una regresión estructural cubre el contrato. El commit de
cierre no fue revertido y los tres jobs obligatorios de CI en `6090bd6`
pasaron.

## Detalle

Ver `spec.md`, `plan.md`, `tasks.md`, `decision.md`, `test-report-1.md`, `code-review-1.md` y `audit-1.md`.
