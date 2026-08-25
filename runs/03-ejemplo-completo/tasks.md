# Tasks: Ejemplo Completo del Circuito Agentico

- **T-01** — Crear estructura de directorios y archivos base
  - Verificacion: `mkdir -p runs/03-ejemplo-completo/docs/{tecnica,usuario}`
  - Traza: AC-1, AC-2, AC-3, AC-4

- **T-02** — Escribir spec.md con identificacion y criterios de aceptacion
  - Verificacion: `python3 -c "json.load(open('spec.md'))"` validar estructura minima
  - Traza: AC-1 a AC-7

- **T-03** — Escribir plan.md con arquitectura, componentes, compatibilidad, dependencias, impacto operacional y estrategia de tests
  - Verificacion: Revisar que las 6 dimensiones esten cubiertas
  - Traza: AC-3

- **T-04** — Escribir decision.md con decisiones demostrables (sin afirmar merge aprobado)
  - Verificacion: `grep -i "merge aprobado" runs/03-ejemplo-completo/decision.md || echo "OK: no afirma merge"`
  - Traza: AC-5

- **T-05** — Ejecutar analyst-agent para producir spec/plan/tasks (simulado)
  - Verificacion: `ls runs/03-ejemplo-completo/spec.md plan.md tasks.md`
  - Traza: AC-1 a AC-4

- **T-06** — Validar circuits contract con Assert-FeatureContract
  - Verificacion: `pwsh NoProfile -ExecutionPolicy Bypass -Command "`. (Join-Path '.\scripts' 'feature-contract.ps1'); Assert-FeatureContract -Slug '03-ejemplo-completo' -Title 'Ejemplo Completo'" 2>&1 | findstr "Falta"` o exit code 0
  - Traza: AC-1 a AC-7

- **T-07** — Poblar docs/tecnica/ejemplo-completo.md y docs/usuario/ejemplo-completo.md
  - Verificacion: `test -s docs/tecnica/ejemplo-completo.md && test -s docs/usuario/ejemplo-completo.md`
  - Traza: AC-1, AC-2

- **T-08** — Actualizar ROADMAP.md con entrada `[ ] 03-ejemplo-completo - Ejemplo complet`
  - Verificacion: `grep -m1 "03-ejemplo-completo" ROADMAP.md`
  - Traza: AC-7

- **T-09** — Ejecutar ready-for-pr.ps1 para marcar READY_FOR_PR y crear PR
  - Verificacion: Revisar en GitHub que PR se creo correctamente
  - Traza: Flujo completo circuito

- **T-10** — Verificar que codigo review y QA pasan antes de merge
  - Verificacion: `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\wait-pr-ci.ps1`
  - Traza: Post-HITL gate