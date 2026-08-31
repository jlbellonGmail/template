# Quality Score History

| Fecha | Commit | Tag | Perfil | Framework | Estado | Score bruto | Score final | Confianza | B | C | M | m | Informe |
|---|---|---|---|---|---|---:|---:|---|---:|---:|---:|---:|---|
| 2026-08-29 | 05ce680 | - | TEMPLATE 1.0 | 1.0 | BASELINE PROVISIONAL | 80.87 | 79.00 | ALTA | 0 | 1 | 2 | 4 | ../reports/AUDIT-2026-08-29-05ce680-baseline-provisional.md |
| 2026-08-30 | 34773af | - | TEMPLATE 1.1 | 1.1 | BASELINE | 92.75 | 79.00 | ALTA | 0 | 1 | 2 | 2 | ../reports/AUDIT-2026-08-30-34773af-baseline-v1-1.md |
| 2026-08-31 | 7964013 | - | TEMPLATE 1.1 | 1.1 | REAUDITORÍA PROVISIONAL — REQUIERE REVISIÓN | 95.50 | 95.50 | ALTA | 0 | 0 | 2 | 0 | ../reports/AUDIT-2026-08-31-7964013-reauditoria-v1-1.md |

## Estado de esta auditoría

Esta fue la primera auditoría piloto ejecutada con el framework `.audit/`.

Durante su revisión posterior se detectaron inconsistencias metodológicas en la
versión 1.0 del framework, entre ellas:

- `SUGGESTION` asociadas a pérdida de puntos;
- camino matemático a 100 incompleto;
- criterios contextuales interpretados de forma demasiado rígida;
- asociaciones inconsistentes entre hallazgos y subcriterios.

Por este motivo el resultado se conserva únicamente como:

`BASELINE PROVISIONAL`

y no debe utilizarse como baseline oficial ni como punto oficial de comparación.

## Primera BASELINE oficial (framework 1.1)

La auditoría del 2026-08-30 sobre el commit `34773af` se ejecutó de forma
independiente con el framework 1.1 ya corregido, cumplió las siete
condiciones mínimas de `.audit/history/README.md` §27 (commit
identificado, framework/perfil identificados, auditoría completa,
consistencia metodológica `PASS`, camino a 100 matemáticamente exacto,
informe y evidencia relacionados, confianza `ALTA`), y se registra como
la primera `BASELINE` oficial del proyecto. Ver
`../reports/AUDIT-2026-08-30-34773af-baseline-v1-1.md` para el detalle
completo, incluida la comparación explícita de divergencias con la
auditoría provisional anterior (realizada solo después de completar la
puntuación propia, sin usarla como entrada).

**Nota de corrección post-emisión (dos rondas):** el score bruto
registrado (92.75) refleja dos revisiones metodológicas aplicadas sobre
el mismo commit `34773af` después de la emisión inicial del informe:

1. Primera ronda: 92.09 → 92.25 (Q6.5 estaba incorrectamente marcado
   `N/A`; el perfil TEMPLATE lo hace aplicable por "documentación
   compilada").
2. Segunda ronda: 92.25 → 92.75 (Q6.5 penalizaba la falta de ejecución
   histórica del pipeline de despliegue de `docs.yml`, pese a existir
   evidencia directa y ejecutable de que el build es reproducible —
   `mkdocs build --strict` con éxito real. Q6.5 pasó a COMPLETO).

Ambas correcciones están documentadas íntegramente, cada una con su
propia validación de consistencia repetida (`PASS`), en las dos
"ADENDA DE CORRECCIÓN METODOLÓGICA" al inicio de
`../reports/AUDIT-2026-08-30-34773af-baseline-v1-1.md`. El score final
(79.00) no cambió en ninguna de las dos rondas porque el mismo Quality
Gate G2 (F-004, CRITICAL) era, y sigue siendo, más restrictivo que el
score bruto en las tres versiones (92.09 → 92.25 → 92.75, todas > 79).

## Reauditoría independiente post-remediación (2026-08-31, commit `7964013`)

Reauditoría ejecutada de forma independiente sobre el commit `7964013`
(punta de `origin/develop` en el momento de la auditoría), posterior a
la remediación de los 5 hallazgos puntuables de la baseline oficial
anterior (`34773af`) y a una corrección adicional de permisos sobre
`guard-develop-branch.yml` (commit `155b9cb`). Se ejecutó sin usar el
score, severidades ni conclusiones de la baseline anterior como
entrada; la comparación histórica se realizó únicamente después de
consolidar el resultado propio. Ver
`../reports/AUDIT-2026-08-31-7964013-reauditoria-v1-1.md` para el
detalle completo, incluida la reverificación independiente (no solo
aceptación por confianza) de los 5 hallazgos históricos y la
identificación de 2 hallazgos MAJOR nuevos (F-001, F-002, misma causa
raíz: la rama `main` declarada en `AGENTS.md` no existe en el
repositorio).

El único Quality Gate que limitaba el score final de la baseline
anterior (G2, por el CRITICAL F-004: sin enforcement técnico real
contra push directo a `develop`) está **liberado**: `guard-develop-branch.yml`
se verificó con evidencia de ejecución real (una corrida exitosa
posterior al fix de permisos, y una corrida histórica fallida que
expuso y confirmó el bug ahora corregido), no solo por inspección
estática. Score final = score bruto = 95.50/100, sin Quality Gate
activo.

### Marcado como PROVISIONAL — REQUIERE REVISIÓN (2026-08-31, mismo commit `7964013`)

Sin recalcular el score: una revisión posterior detectó que los
hallazgos F-001/F-002 de esta reauditoría (rama `main` inexistente y
su consecuencia sobre `docs.yml`/GitHub Pages) pueden estar
penalizando como capacidades **actuales y obligatorias** algo que
podría ser legítimamente **prospectivo**, con el mismo criterio que
`AUDIT_RULES.md` §45/§62 y `QUALITY_SCORE.md` §10 ya reconocen para
versionado/releases no ejercidos — criterio que este mismo informe
aplicó a Q6.4 (sin penalizar la ausencia de release real, dado que
`ROADMAP.md` declara "Por definir... no tiene producto propio
todavía") pero no de forma evidentemente consistente a F-001/F-002.

El score 95.50/100 se conserva íntegro como resultado histórico de
esta ejecución. La evidencia (`../evidence/2026-08-31-7964013-reauditoria-v1-1/`)
permanece intacta. Ver la nota completa al inicio de
`../reports/AUDIT-2026-08-31-7964013-reauditoria-v1-1.md`
("ESTADO DE ESTE INFORME"). Este resultado **no debe usarse como
baseline oficial** hasta que la revisión dedicada de F-001/F-002 se
complete y, si corresponde, se registre como una nueva entrada en esta
tabla (no como una edición retroactiva de la fila `7964013`).

## Convenciones

- **B** = BLOCKER
- **C** = CRITICAL
- **M** = MAJOR
- **m** = MINOR

Las `SUGGESTION` no forman parte del score histórico porque no restan puntos.
