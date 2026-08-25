# Decisiones de diseño e implementacion - Ejemplo Completo

Este documento describe las decisiones de diseño tomadas al implementar
el ejemplo completo del circuito agentico AI-Native.

## Decisiones tomadas

1. **Circuito de 5 agentes**: Se mantuvo el orden Analyst → Reviewer → Builder → QA → Code Reviewer, con HITL unico humano en la decision MERGE/NO MERGE de la PR.

2. **SDD formal**: Se adicionaron `plan.md` y `tasks.md` como artefactos obligatorios producidos por `analyst-agent`, con trazabilidad AC-N en todo momento.

3. **Validacion de schemas JSON**: Se implementaron `.agentic/schemas/agents.schema.json`, `.agentic/schemas/models.schema.json` y `.agentic/schemas/work-unit.schema.json` para validar estructura de `.agentic/agents.json` y `.agentic/models.json`.

4. **Modos soportados**: El circuito soporta dos modos: `Feature` (item unico NN-slug en ROADMAP.md) y `Milestone` (multiples items agrupados bajo work-unit.json).

5. **Post-HITL gate**: Se adiciono validacion automatica en `.github/workflows/post-hitl-merge-gate.yml` que verifica que el humano sigue aprobado y los checks de CI siguen verdes antes de mergear.

6. **Cierre post-merge**: `scripts/close-feature.ps1` cambia automaticamente `[-]` a `[x]` en ROADMAP.md despues de mergear a develop, con idempotencia (reejecuciones no crean commits duplicados).

7. **No se asume stack**: Segun `AGENTS.md` y `docs/tecnica/arquitectura.md`, no se agregan backends, bases de datos ni dependencias de build sin decision arquitectonica explcita.

## Casos borde

- Rechazo de `code-reviewer-agent` vuelve a `builder-agent` -> `qa-agent`, nunca a `analyst-agent`.
- States `ROADMAP.md` `[ ]` / `[-]` / `[x]` deben respetarse exactamente, no hay estados intermedios.
- `New-DecisionFile` nunca escribe "MERGE aprobado", solo referencia a HITL/GitHub.

## Referencias

- `AGENTS.md` - Reglas compartidas del repositorio
- `ROADMAP.md` - Estado verificado de features
- `docs/producto/contexto-producto.md` - Conocimiento funcional persistente