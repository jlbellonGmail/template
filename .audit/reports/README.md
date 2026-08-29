# Audit Reports

**Versión:** 1.0
**Estado:** Activo

---

# 1. Propósito

La carpeta:

```text
.audit/reports/
```

almacena los informes finales de auditoría.

Cada informe representa la evaluación de un estado concreto del repositorio utilizando versiones concretas del framework.

Los informes son históricos.

No deben sobrescribirse para reflejar correcciones posteriores.

---

# 2. Unidad de informe

Cada auditoría completa debe generar un informe independiente.

Formato recomendado:

```text
AUDIT-YYYY-MM-DD-<short-commit>-<slug>.md
```

Ejemplo:

```text
AUDIT-2026-08-29-a12b34c.md
```

Si no existe commit:

```text
AUDIT-YYYY-MM-DD-WORKTREE.md
```

---

# 3. Colisiones de nombre

Si se realizan varias auditorías sobre el mismo commit y fecha:

utilizar un sufijo.

Ejemplo:

```text
AUDIT-2026-08-29-a12b34c-01.md
AUDIT-2026-08-29-a12b34c-02.md
```

Si son auditores distintos puede utilizarse:

```text
AUDIT-2026-08-29-a12b34c-CODEX.md
AUDIT-2026-08-29-a12b34c-CLAUDE.md
```

cuando sea útil para auditoría cruzada.

---

# 4. No usar `latest.md` como fuente histórica

Puede existir opcionalmente un puntero o índice al informe actual.

Pero el informe histórico real debe conservar nombre único.

No debe reemplazarse silenciosamente:

```text
latest.md
```

perdiendo trazabilidad.

---

# 5. Identificación obligatoria

Todo informe debe indicar:

```text
Repositorio:
Ruta:
Branch:
Commit:
Tag:
Fecha:
Worktree:
Perfil:
QUALITY_SCORE:
AUDIT_RULES:
Versión de perfil:
Auditor:
Entorno:
Confianza:
```

Cuando un dato no pueda determinarse:

```text
NO DETERMINADO
```

---

# 6. Estructura mínima

Los informes generados mediante `AUDIT_PROMPT.md` deben contener:

```text
A. IDENTIFICACIÓN
B. VEREDICTO EJECUTIVO
C. ALCANCE Y LIMITACIONES
D. CONTRATO DETECTADO
E. MATRIZ DE PUNTUACIÓN
F. DETALLE POR SUBCRITERIO
G. LEDGER DE VERIFICACIÓN
H. HALLAZGOS
I. CAUSAS RAÍZ
J. QUÉ SOBRA
K. QUÉ FALTA
L. NO VERIFICADO
M. QUALITY GATES
N. CAMINO MATEMÁTICO A 100
O. PLAN DE REMEDIACIÓN
P. SEGUNDA PASADA DE 100
Q. CERTIFICACIÓN FINAL
```

No deben omitirse silenciosamente secciones obligatorias.

---

# 7. Score

Todo informe debe mostrar separadamente:

```text
Score bruto
Score final
```

Cuando existan N/A:

también:

```text
Puntos aplicables
Score normalizado
```

Cuando exista Quality Gate:

indicar cuál.

---

# 8. Hallazgos

Cada hallazgo debe tener ID estable dentro del informe.

Formato:

```text
F-001
F-002
F-003
```

Un hallazgo debe conservar su ID dentro del mismo informe.

No reutilizar IDs para problemas diferentes.

---

# 9. Hallazgos históricos

Los IDs no necesitan ser globalmente únicos entre auditorías.

Por ejemplo:

```text
AUDIT A → F-001
AUDIT B → F-001
```

son válidos porque cada informe tiene su propio contexto.

Si se necesita trazabilidad longitudinal puede añadirse posteriormente un identificador persistente.

---

# 10. Evidencia

Los informes deben referenciar la carpeta correspondiente:

```text
.audit/evidence/YYYY-MM-DD-<short-commit>/
```

Ejemplo:

```text
Evidencia:
../evidence/2026-08-29-a12b34c/tests.txt
```

No copiar dentro del informe salidas extensas sin necesidad.

---

# 11. Informe inmutable

Después de completado y aceptado como resultado histórico:

el informe no debe modificarse para aparentar que el proyecto auditado era diferente.

Si se detecta un error material en el informe:

preferir:

* emitir una corrección explícita;
* o ejecutar nueva auditoría.

---

# 12. Correcciones posteriores

Un hallazgo corregido posteriormente no debe borrarse del informe original.

El informe representa:

```text
estado en commit X
```

La corrección debe aparecer en:

```text
nuevo commit
→ nueva auditoría
→ nuevo informe
```

---

# 13. Auditoría parcial

Si una auditoría no pudo completarse:

el nombre puede utilizar:

```text
AUDIT-PARTIAL-YYYY-MM-DD-<commit>.md
```

y debe indicar claramente:

```text
ESTADO: PARCIAL
```

No debe confundirse con una auditoría completa.

---

# 14. Auditoría invalidada

Si se descubre que la metodología utilizada era incorrecta o que se auditó el commit equivocado:

el informe debe marcarse:

```text
INVALIDADO
```

No eliminarlo silenciosamente si ya forma parte del historial relevante.

Debe explicarse el motivo.

---

# 15. Auditoría cruzada

Cuando exista más de un auditor sobre el mismo estado:

conservar todos los informes independientes.

Posteriormente puede generarse:

```text
CONSENSUS-YYYY-MM-DD-<commit>.md
```

para resolver divergencias.

El informe de consenso no reemplaza los originales.

---

# 16. Informe de consenso

Un informe de consenso debe indicar:

```text
Auditorías comparadas:
Discrepancias:
Evidencia revisada:
Resoluciones:
Score resultante:
```

No debe simplemente promediar las notas.

---

# 17. Reauditoría

Después de correcciones:

crear siempre un nuevo informe.

Ejemplo:

```text
AUDIT-2026-08-29-a12b34c.md → 83/100

correcciones

AUDIT-2026-09-02-c45d67e.md → 96/100
```

Ambos deben conservarse.

---

# 18. Plan a 100

Si el score es inferior a 100, el informe debe indicar:

```text
Score actual
Hallazgos puntuables
Puntos recuperables
Score esperado
```

La suma debe ser consistente.

---

# 19. Mejoras opcionales

Las SUGGESTION deben quedar claramente separadas de los defectos puntuables.

Nunca debe implicarse que son necesarias para obtener 100/100 si no restaron puntos.

---

# 20. Certificación interna del framework

La frase:

```text
TEMPLATE DE REFERENCIA 100/100
```

sólo puede utilizarse cuando se cumplen todas las condiciones definidas por:

```text
QUALITY_SCORE.md
AUDIT_RULES.md
profiles/TEMPLATE.md
```

No representa una certificación oficial externa.

---

# 21. Resumen ejecutivo

El resumen ejecutivo debe ser breve y útil.

Debe responder:

```text
¿Cuál es el score?
¿Cuál es el principal riesgo?
¿Qué impide 100?
¿Puede utilizarse el proyecto?
```

El detalle técnico pertenece a las secciones posteriores.

---

# 22. Objetividad

Los informes deben evitar expresiones vagas como:

```text
“muy bueno”
“bastante profesional”
“parece excelente”
```

sin explicación.

Preferir:

```text
Q5.3 = 4/4
Tests oficiales ejecutados:
327 passed
```

---

# 23. No ocultar incertidumbre

Debe mostrarse explícitamente:

```text
NO VERIFICADO
EVIDENCIA INSUFICIENTE
NO DETERMINADO
```

cuando corresponda.

Un informe profesional no necesita aparentar certeza absoluta.

---

# 24. Referencias a archivos

Cuando sea posible utilizar rutas concretas.

Ejemplo:

```text
.github/workflows/ci.yml
scripts/validate.ps1
AGENTS.md
```

Esto facilita reproducibilidad.

---

# 25. Regla final

Un informe debe permitir a una persona que no participó en la auditoría comprender:

> por qué el proyecto obtuvo exactamente esa puntuación y qué evidencia sostiene cada desviación relevante.
