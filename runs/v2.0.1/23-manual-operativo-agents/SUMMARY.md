# Resumen de la unidad

Estado: READY_FOR_PR
Versión: v2.0.1
Tipo: Feature
SDD: LIGHT
PR: pendiente de creación
Merge: pendiente de decisión HITL

## Objetivo

Convertir `AGENTS.md` en un manual operativo breve y suficiente sin cambiar
el comportamiento funcional, los gates, la compatibilidad ni la seguridad del
Template.

## Resultado

`AGENTS.md` fue reorganizado desde 1.074 líneas a un manual conciso con
referencias canónicas. El backlog agrega `23-manual-operativo-agents` bajo
v2.0.1. No se modificaron scripts, workflows, adaptadores ni tags históricos.

## Cambios principales

- Se conservaron las reglas de reentrada, autoridad, roles, work units,
  ASSESS/SDD adaptativo, circuito, contratos, HITL, Git, CI y seguridad.
- Se eliminaron duplicaciones, historia ya congelada y listados que pertenecen
  a `scripts/`, `CONSTITUTION.md` o documentación técnica existente.
- Se agregó evidencia ASSESS/SDD LIGHT y mini-spec en este run.

## Validación

Pendiente durante la construcción; el reporte reproducible de comandos y
resultados se registrará en `test-report-1.md` si el contrato lo exige. La
revisión vigente está en `code-review-1.md`.

## Decisiones

- Se respetó literalmente la profundidad LIGHT producida por ASSESS (riesgo
  LOW, dos rutas documentales, score 0); no se creó evidencia opcional como
  placeholder.
- La release v2.0.1 requiere una decisión humana posterior sobre la PR y el
  commit candidato; esta unidad no autoriza merge ni tag.

## Incidencias

Ninguna incidencia técnica conocida. La unidad queda detenida sólo cuando
corresponde por el HITL final.

## Detalle

Evidencia máquina: `assess.jsonl`, `sdd.json` y `sdd-evidence.jsonl`. La
revisión debe comprobar que los enlaces canónicos y los nombres de jobs
documentados coincidan con los archivos reales.
