# F04 — Convergence autónoma Builder–Reviewer

Estado: implementada, pendiente de PR y merge  
Versión: v2.0.0  
Tipo: Feature  
PR: pendiente  
Merge: pendiente

## Objetivo
Coordinar correcciones Builder ↔ Reviewer con progreso verificable y salida
segura.

## Resultado
Contrato JSON determinístico con aprobación, escalamiento, bloqueo y fallo
seguro; ciclos proporcionales a ASSESS/SDD.

## Cambios principales
`scripts/convergence.ps1`, pruebas pytest y documentación mínima técnica y de
usuario.

## Validación
4 escenarios pytest pasan; incluye perfiles LIGHT/STANDARD/FULL y protección
contra estancamiento.

## Decisiones
Presupuesto por defecto 2/4/6; `MaxIterations` permite extensión sin acoplar
modelos. Reviewer permanece independiente y Builder no aprueba.

## Incidencias
Ninguna conocida.

## Detalle
[spec](spec.md) · [plan](plan.md) · [tasks](tasks.md) · [audit](audit-1.md) ·
[QA](test-report-1.md) · [code review](code-review-1.md) · [decision](decision.md)

## Paralelización futura
F05 consume esta salida para formalizar evidencias; F06 y F07 dependen de
contratos/evidencia posteriores. F08 puede avanzar cuando sus prerrequisitos
propios estén cerrados, sin iniciar aquí ninguna fase.
