# Spec: Ejemplo Completo del Circuito Agentico

## Identificacion

- Work unit: 03-ejemplo-completo
- Modo: FEATURE
- Items: (ninguno - feature individual)

## Alcance

Incluye la implementacion completa de una feature mediante el circuito agentico:
Analista -> Auditor -> Implementador -> QA -> Code Reviewer -> READY_FOR_PR.

Explicitamente NO incluye:
- Automatizar branch protection de GitHub
- Agregar un tercer modo EPIC
- Modelos de LLM reales

## Contexto y fuentes

Consultado ROADMAP.md item 03-ejemplo-completo, analisis de AGENTS.md,
revision de docs/tecnica/arquitectura.md y scripts/*.ps1 existentes. El circuito
ya se encuentra en estado 100% funcional con 194 tests pytest y 5 subagentes
implementados (Analyst, Reviewer, Builder, QA, Code-Reviewer).

## Criterios de aceptacion

- **AC-1**: Existe `docs/tecnica/ejemplo-completo.md` no vacio con decisiones de diseno
- **AC-2**: Existe `docs/usuario/ejemplo-completo.md` no vacio con proposito y uso
- **AC-3**: Existe `runs/03-ejemplo-completo/plan.md` con estrategia de implementacion
- **AC-4**: Existe `runs/03-ejemplo-completo/tasks.md` con tareas trazables a AC
- **AC-5**: Existe `runs/03-ejemplo-completo/decision.md` con decisiones demostrables
- **AC-6**: `docs/tecnica/index.md` y `docs/usuario/index.md` tienen enlaces exactos
- **AC-7**: ROADMAP.md tiene entrada `[ ] 03-ejemplo-completo - Ejemplo complet`

## Casos borde a contemplar

- Un `audit-N.md` con status distino de `approved` o `rejected` tratado como malformado
- Numeracion no contigua de intentos (`audit-1.md`, `audit-3.md`, sin `audit-2.md`)
- `code-review-N.md` ausente completamente debe fallar el contrato

## Supuestos

- PowerShell 7+ y Git estan disponibles en el entorno
- GitHub CLI (`gh`) esta autenticado para operacion de PRs
- No hay stack de producto definido (decision en `docs/tecnica/arquitectura.md`)

## Clarificaciones realizadas

Vacio - no habian ambiguedades materiales que resolver.

## Decisiones pendientes bloqueantes

Vacio - no hay ambigedades sin resolver.