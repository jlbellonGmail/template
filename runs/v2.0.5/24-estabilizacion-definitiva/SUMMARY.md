# 24-estabilizacion-definitiva

Estado: READY_FOR_PR
Versión: v2.0.5
Tipo: Feature
SDD: FULL
PR: PENDING
Merge: PENDING

## Objetivo

Estabilizar Template v2.0.5 corrigiendo STATUS-only, integridad de runs no canónicos y distribución/upgrades de consumidores.

## Resultado

Implementado localmente y validado con suite completa. Pendiente PR, CI remoto, merge HITL, tag/release v2.0.5 y validación post-release.

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
- `check-status.ps1`: PASS.
- `check-integrity.ps1 -Version v2.0.5`: PASS.

## Decisiones

El upgrade copia únicamente `sharedPaths`; los consumidores anteriores sin `templateVersion` deben informar `-BaselineVersion`.

## Incidencias

Dos corridas completas tuvieron un fallo transitorio de permisos Git en `%TEMP%` al pushear a bare repos temporales; ambos tests exactos pasaron al reintentar. La segunda suite completa pasó completa antes de agregar evidencia.

## Detalle

Ver `spec.md`, `plan.md`, `tasks.md`, `decision.md`, `test-report-1.md`, `code-review-1.md` y `audit-1.md`.
