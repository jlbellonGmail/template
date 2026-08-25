# Guia de usuario - Ejemplo Completo del Circuito Agentico

## Para que sirve

Este ejemplo demuestra como funciona el circuito agentico AI-Native desde
el momento en que se crea una feature hasta que se cierra automaticamente
despues del merge a `develop`.

## Circuito descripto

1. **Analyst-agent**: Produce `spec.md`, `plan.md` y `tasks.md` describiendo QUÉ,
   CÓMO y QUÉ TAREAS componen la feature.

2. **Reviewer-agent**: Audita los tres artefactos juntos y emite veredicto
   `approved` o `rejected`. 4 rechazos automáticos no negociables.

3. **Builder-agent**: Implementa el codigo y escribe `docs/tecnica/<slug>.md`
   + `docs/usuario/<slug>.md` + `decision.md`.

4. **QA-agent**: Corre tests (pytest + scripts del circuito) y verifica el
   contrato comun. Emite `test-report-N.md`.

5. **Code-Reviewer-agent**: Revisa el diff FINAL (codigo, tests, scripts,
   config, docs afectada) despues de QA. Emite `code-review-N.md`.

6. **READY_FOR_PR**: `ready-for-pr.ps1` marca ROADMAP.md con `[-]` y crea PR
   hacia `develop` con evidencias completas.

7. **HITL ( unico punto humano)**: El humano aprueba o rechaza la PR en GitHub.

8. **Post-HITL gate**: GitHub Actions verifica que la aprobacion sigue vigente
   y los checks de CI estan verdes, entonces mergea.

9. **Post-merge close**: GitHub Actions ejecuta `close-feature.ps1` que cambia
   `[-]` a `[x]` en ROADMAP.md y limpia worktrees/localmente.

## Como usar este ejemplo

- Revisar `ROADMAP.md` para ver el item `03-ejemplo-completo - Ejemplo complet`
- Ejecutar `scripts\start-work-unit.ps1 -Mode Feature -Slug 03-ejemplo-completo`
- Seguir los steps en `tasks.md` marcado T-01 a T-10
- Aprobar la PR en GitHub para disparar el merge automático
- Ver que ROADMAP.md cambia automaticamente a `[x]`

## Terminologia clave

- **WorkUnit**: Feature individual o Milestone agrupado
- **SDD**: Spec-Driven Development (spec→plan→tasks)
- **HITL**: Human-in-the-loop (decision MERGE/NO MERGE)
- **ROADMAP.md**: Mapa con estados `[ ]` pendiente, `[-]` READY_FOR_PR, `[x]` completado
- **Post-HITL gate**: Validacion automatica post-aprobacion humana