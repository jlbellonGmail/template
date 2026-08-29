# Evidence

**Versión:** 1.0
**Estado:** Activo

---

# 1. Propósito

La carpeta:

```text
.audit/evidence/
```

almacena evidencia generada o recopilada durante las auditorías.

Su objetivo es permitir que las conclusiones importantes de un informe puedan:

* verificarse;
* reproducirse;
* auditarse posteriormente;
* compararse entre ejecuciones.

La evidencia complementa al informe.

No reemplaza al informe.

---

# 2. Principio

Toda evidencia debe responder a una pregunta concreta de auditoría.

No deben almacenarse archivos simplemente porque puedan generarse.

La regla es:

```text
EVIDENCIA ÚTIL
=
evidencia necesaria para sostener,
reproducir o verificar una conclusión
```

---

# 3. Qué puede almacenarse

Según el proyecto pueden conservarse:

```text
estructura del repositorio
estado Git
branches
tags
resultados de tests
resultados de lint
resultados de build
resultados de bootstrap
resultados de regresión
validaciones
escaneos de seguridad
configuración remota verificada
inventarios
resultados de scripts
matrices de verificación
```

Ejemplos:

```text
repository-tree.txt
git-status.txt
git-branches.txt
git-tags.txt
tests.txt
lint.txt
build.txt
bootstrap.txt
regression.txt
security.txt
github-controls.md
verification.md
```

No existe una lista obligatoria universal.

---

# 4. Organización por auditoría

La evidencia debe organizarse preferentemente por auditoría.

Formato:

```text
.audit/evidence/
└── YYYY-MM-DD-<short-commit>-<slug>/
```

Ejemplo:

```text
.audit/evidence/
└── 2026-08-29-a12b34c/
    ├── repository-tree.txt
    ├── git-status.txt
    ├── tests.txt
    ├── lint.txt
    └── verification.md
```

Si no existe commit identificable:

```text
YYYY-MM-DD-WORKTREE/
```

Ejemplo:

```text
.audit/evidence/
└── 2026-08-29-WORKTREE/
```

---

# 5. Relación con el informe

Cada carpeta de evidencia debe corresponder a un informe.

Ejemplo:

```text
.audit/reports/
AUDIT-2026-08-29-a12b34c.md

.audit/evidence/
2026-08-29-a12b34c/
```

El informe debe referenciar la evidencia relevante.

---

# 6. Convención de nombres

Los nombres deben ser:

* cortos;
* descriptivos;
* estables;
* sin espacios innecesarios.

Formato recomendado:

```text
<tipo>-<detalle>.<ext>
```

Ejemplos:

```text
tests-unit.txt
tests-regression.txt
build-main.txt
lint-markdown.txt
security-dependencies.txt
github-rulesets.md
```

---

# 7. Evidencia textual

Siempre que sea suficiente debe preferirse texto plano o Markdown.

Formatos recomendados:

```text
.txt
.md
.json
```

Esto facilita:

* revisión;
* diff;
* búsqueda;
* reutilización por otros agentes.

---

# 8. Salidas grandes

No debe copiarse indiscriminadamente toda salida extensa.

Si una herramienta genera miles de líneas:

conservar sólo cuando sea necesario para reproducibilidad o diagnóstico.

El informe debe resumir el resultado.

Ejemplo:

```text
pytest:
327 passed
0 failed
```

La salida completa puede conservarse en:

```text
tests.txt
```

si aporta valor.

---

# 9. Registro mínimo de una ejecución

Cuando una evidencia provenga de un comando debería incluir, cuando sea posible:

```text
Comando:
Fecha:
Entorno:
Exit code:
Resultado:
Estado:
```

Ejemplo:

```text
Comando:
python -m pytest

Exit code:
0

Resultado:
327 passed

Estado:
PASS
```

---

# 10. Evidencia manual

Algunas verificaciones pueden requerir inspección manual.

Ejemplo:

```text
github-controls.md
```

Puede registrar:

```text
Branch:
main

Required PR:
VERIFICADO

Required checks:
VERIFICADO

Force push:
BLOQUEADO

Fuente:
configuración remota inspeccionada
```

Debe diferenciar claramente:

```text
VERIFICADO
```

de:

```text
DOCUMENTADO
```

---

# 11. Evidencia sensible

Nunca deben almacenarse secretos completos.

No conservar:

* tokens;
* contraseñas;
* private keys;
* cookies;
* credenciales;
* connection strings sensibles.

Si deben documentarse:

usar redacción.

Ejemplo:

```text
ghp_****abcd
```

---

# 12. Datos personales

No conservar datos personales innecesarios.

Cuando una evidencia contenga información sensible:

* anonimizar;
* redactar;
* resumir;

cuando sea posible sin perder utilidad técnica.

---

# 13. Evidencia externa

Si una conclusión depende de una plataforma externa puede registrarse:

```text
servicio
fecha
configuración observada
resultado
```

Ejemplos:

* GitHub;
* registry;
* CI externo;
* package manager.

No debe almacenarse información privada innecesaria.

---

# 14. Evidencia temporal

Algunas pruebas pueden generar archivos temporales.

Si no son necesarios después de consolidar la auditoría:

deben eliminarse.

La carpeta `evidence/` no debe convertirse en un depósito de basura.

---

# 15. Evidencia reproducible

Siempre que sea posible debe preferirse evidencia que otro auditor pueda reproducir.

Ejemplo fuerte:

```text
Comando:
./scripts/validate

Exit code:
0
```

frente a:

```text
“Funcionó correctamente.”
```

---

# 16. Evidencia derivada

Una evidencia generada a partir de otra debe indicarlo cuando sea relevante.

Ejemplo:

```text
summary-tests.md
```

derivado de:

```text
tests-full.txt
```

La evidencia derivada no debe ocultar resultados negativos presentes en la fuente original.

---

# 17. Integridad

No debe alterarse una evidencia después de emitido el informe para cambiar retrospectivamente el resultado.

Si se descubre un error:

* generar nueva evidencia;
* realizar nueva auditoría o corrección explícita;
* mantener trazabilidad.

---

# 18. Evidencia histórica

Las evidencias anteriores deben considerarse históricas.

No demuestran automáticamente el estado actual.

Ejemplo:

```text
tests PASS
```

en un commit anterior no significa:

```text
tests PASS
```

en el commit actual.

---

# 19. Reauditorías

Cada reauditoría debe generar su propia carpeta cuando exista nueva evidencia.

Ejemplo:

```text
2026-08-29-a12b34c/
2026-09-02-c45d67e/
```

No sobrescribir resultados históricos.

---

# 20. Qué no guardar

Evitar:

```text
node_modules/
venv/
binarios completos
caches
builds temporales
logs sin utilidad
copias del repositorio
archivos gigantes sin propósito
secretos
```

salvo que una evidencia concreta lo requiera excepcionalmente.

---

# 21. Relación con Git

La política de versionado de evidencias debe ser coherente con el tamaño y sensibilidad del proyecto.

Evidencia:

* pequeña;
* textual;
* útil históricamente;

puede versionarse.

Evidencia:

* masiva;
* sensible;
* fácilmente regenerable;

puede excluirse del repositorio.

La decisión debe documentarse si es relevante.

---

# 22. Evidencia mínima recomendada

Para una auditoría TEMPLATE profunda considerar, cuando aplique:

```text
repository-tree.txt
git-status.txt
git-branches.txt
git-tags.txt
validation.txt
tests.txt
build.txt
bootstrap.txt
security.txt
remote-controls.md
verification.md
```

No crear archivos vacíos sólo para cumplir esta lista.

---

# 23. `verification.md`

Puede utilizarse como ledger resumido de evidencia.

Formato recomendado:

| ID    | Verificación      | Resultado  | Estado | Evidencia          |
| ----- | ----------------- | ---------- | ------ | ------------------ |
| V-001 | Tests             | 327 passed | PASS   | tests.txt          |
| V-002 | Build             | Exit 0     | PASS   | build.txt          |
| V-003 | Branch protection | Verificada | PASS   | remote-controls.md |

---

# 24. Regla final

La carpeta `evidence/` debe contener:

> la evidencia suficiente para defender la auditoría,

no:

> toda la información que fue posible recopilar.
