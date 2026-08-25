# Plan: Ejemplo Completo del Circuito Agentico

## 1. Arquitectura afectada

Esta feature toca los siguientes componentes del repositorio:
- `.agentic/roles/*.md` - Roles ya definidos, no se modifican
- `scripts/*.ps1` - Motor ejecutable, posibles mejoras menores
- `docs/tecnica/` y `docs/usuario/` - Documentacion a agregar
- `ROADMAP.md` - Estado del backlog

## 2. Componentes y contratos nuevos/modificados

- **`docs/tecnica/ejemplo-completo.md`**: Decisiones de diseno e implementacion
- **`docs/usuario/ejemplo-completo.md`**: Proposito de la feature, como verla/usarla
- **`runs/03-ejemplo-completo/plan.md`**: Estrategia detallada de implementacion
- **`runs/03-ejemplo-completo/tasks.md`**: Tareas ejecutables y verificables

Cada componente responde a los AC-N de `spec.md` segun siguiente mapeo:
- AC-1..2 -> documentacion tecnica y usuario
- AC-3 -> plan.md secciones 1-3
- AC-4 -> tasks.md T-01 a T-10
- AC-5 -> decision.md decisiones
- AC-6/7 -> indices y ROADMAP.md

## 3. Compatibilidad y migracion

No hay datos/artefactos previos que migrar en este template nuevo.
Se documenta que feature es autocontenida y no afecta features previas.

## 4. Dependencias

- `.agentic/agents.json` - Metadatos de roles y modelos
- `.agentic/models.json` - Router de modelos y fallbacks
- `scripts/feature-contract.ps1` - Validacion comun del circuito
- `scripts/workunit-lib.ps1` - Utilidades shared

## 5. Impacto operacional

- Nuevos archivos que se generan en `runs/03-ejemplo-completo/`
- `ROADMAP.md` cambia de `[ ]` a `[-]` despues de ready-for-pr
- `Rename` necesario: Ninguno - todos los scripts usan convenciones existentes

## 6. Estrategia de tests

- `pytest` sobre `tests/` - validacion del circuito
- `scripts/feature-contract.ps1` - Assert-FeatureContract
- Verificacion manual: `ready-for-pr.ps1` y `close-feature.ps1`

## 7. Verificacion final

Antes de READY_FOR_PR:
- [ ] spec.md existe y tiene todos los AC
- [ ] plan.md existe y cubre arquitectura + componentes + compatibilidad + dependencias + impacto operacional + estrategia de tests
- [ ] tasks.md existe y cada tarea tiene AC-N asociado
- [ ] decision.md existe y no afirma merge aprobado
- [ ] Veredicto ultimo de audit/test-review es `approved`
- [ ] ROADMAP.md tiene entrada `[ ] 03-ejemplo-completo`