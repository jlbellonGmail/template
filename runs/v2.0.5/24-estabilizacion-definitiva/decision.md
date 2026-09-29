# Decision - 24-estabilizacion-definitiva

## Decisión

El upgrade oficial se basa en `scripts/template-starter-manifest.json` como lista positiva de archivos compartidos. El script nuevo exige `TargetVersion`, resuelve `BaselineVersion` desde el manifest del consumidor o por parámetro explícito, valida tags exactos y compara SHA256 de archivos materializados con `core.autocrlf=false`.

## Justificación

Una lista positiva evita copiar estado local o archivos funcionales del consumidor. El baseline explícito elimina versiones hardcodeadas y permite detectar drift confirmado antes de sobrescribir. La comparación por archivos materializados evita falsos resultados por diferencias entre blobs Git y working trees en Windows.

## Consecuencias

Los consumidores anteriores a manifests con `templateVersion` deben pasar `-BaselineVersion` en el primer upgrade. Un cambio local en archivos compartidos falla como drift y requiere reconciliación humana antes de aplicar el upgrade.
