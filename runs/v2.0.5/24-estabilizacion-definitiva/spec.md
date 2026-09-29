# Spec - 24-estabilizacion-definitiva

## Objetivo

Publicar una base v2.0.5 confiable para consumidores del Template, corrigiendo defectos reales detectados durante adopción v2.0.4 y reemplazando scripts externos de upgrade por un mecanismo oficial versionado.

## Alcance

- `check-status.ps1` debe aceptar un HEAD posterior al snapshot cuando el diff desde el HEAD registrado contiene únicamente `STATUS.md`.
- `check-integrity.ps1` debe interpretar como runs canónicos sólo carpetas bajo `runs/vX.Y.Z/`.
- El upgrade de consumidores debe vivir en el repositorio, exigir `TargetVersion`, validar tags exactos, comparar baseline/target contra manifest, copiar sólo `sharedPaths`, preservar archivos funcionales y fallar ante drift o trabajo pendiente.
- La documentación de adopción debe describir el mecanismo oficial.

## Fuera de Alcance

- No modificar CORE, TENANTS, PERSONS, CRM ni otros consumidores reales.
- No copiar `STATUS.md`, `ROADMAP.md`, `runs/` ni releases a consumidores.
- No crear tags/releases desde esta unidad antes del gate humano correspondiente.

## Criterios de Aceptación

- Regresiones específicas cubren STATUS-only commits y runs `Txx` no canónicos.
- Prueba real con repositorios temporales ejecuta upgrade v2.0.4 -> v2.0.5 sobre un consumidor de prueba.
- La suite completa local queda verde.
- `check-status.ps1` y `check-integrity.ps1 -Version v2.0.5` pasan al cierre.
