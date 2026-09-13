# F03 — Arquitectura de roles por capacidades

Estado: lista para PR  
Versión: v2.0.0  
Tipo: Feature  
PR: pendiente  
Merge: pendiente

## Objetivo
Reducir roles conceptuales y desacoplarlos de modelos/proveedores.

## Resultado
Planner, Builder y Reviewer canónicos, con QA y code review como capacidades
del Reviewer y aliases históricos sólo para compatibilidad.

## Cambios principales
Fuente `.agentic/` y adaptadores sincronizados; router, mensaje versionado y
documentación ajustados.

## Validación
pytest, sync `-Check`, contrato y checks de lifecycle aprobados.

## Decisiones
ASSESS y SDD adaptativo se consumen sin duplicarse. F04 permanece pendiente.

## Incidencias
Ninguna conocida.

## Detalle
[spec](spec.md) · [plan](plan.md) · [tasks](tasks.md) · [audit](audit-1.md) · [QA](test-report-1.md) · [code review](code-review-1.md) · [decision](decision.md)
