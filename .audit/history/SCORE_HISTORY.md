# Quality Score History

| Fecha | Commit | Tag | Perfil | Framework | Estado | Score bruto | Score final | Confianza | B | C | M | m | Informe |
|---|---|---|---|---|---|---:|---:|---|---:|---:|---:|---:|---|
| 2026-08-29 | 05ce680 | - | TEMPLATE 1.0 | 1.0 | BASELINE PROVISIONAL | 80.87 | 79.00 | ALTA | 0 | 1 | 2 | 4 | ../reports/AUDIT-2026-08-29-05ce680-baseline-provisional.md |
| 2026-08-30 | 34773af | - | TEMPLATE 1.1 | 1.1 | BASELINE | 92.75 | 79.00 | ALTA | 0 | 1 | 2 | 2 | ../reports/AUDIT-2026-08-30-34773af-baseline-v1-1.md |

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

## Convenciones

- **B** = BLOCKER
- **C** = CRITICAL
- **M** = MAJOR
- **m** = MINOR

Las `SUGGESTION` no forman parte del score histórico porque no restan puntos.
