# Quality Score History

| Fecha | Commit | Tag | Perfil | Framework | Estado | Score bruto | Score final | Confianza | B | C | M | m | Informe |
|---|---|---|---|---|---|---:|---:|---|---:|---:|---:|---:|---|
| 2026-08-29 | 05ce680 | - | TEMPLATE 1.0 | 1.0 | BASELINE PROVISIONAL | 80.87 | 79.00 | ALTA | 0 | 1 | 2 | 4 | ../reports/AUDIT-2026-08-29-05ce680-baseline-provisional.md |

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

La primera `BASELINE` oficial será generada mediante una nueva auditoría completa
utilizando el framework 1.1, una vez validada su consistencia.

## Convenciones

- **B** = BLOCKER
- **C** = CRITICAL
- **M** = MAJOR
- **m** = MINOR

Las `SUGGESTION` no forman parte del score histórico porque no restan puntos.
