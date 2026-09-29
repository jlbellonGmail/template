# Plan - 24-estabilizacion-definitiva

1. Confirmar estado real de Git/GitHub y reproducir los defectos reportados.
2. Limitar integridad a runs canónicos y conservar cobertura para orphan runs reales.
3. Incorporar upgrade oficial de consumidores con manifest, tag exacto, baseline anti-drift e idempotencia.
4. Actualizar manifest y guías de adopción/status.
5. Agregar regresiones y prueba de upgrade v2.0.4 -> v2.0.5.
6. Ejecutar pruebas focalizadas, suite completa, `check-status` y `check-integrity`.
7. Preparar PR; el merge y release quedan sujetos al HITL requerido por el Template.
