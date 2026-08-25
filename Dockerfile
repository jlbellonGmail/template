# Dockerfile - Template AI-Native Agentico
# =============================================
# Imagen base: Python 3.12 + PowerShell 7 para scripts agenticos
# Propósito: Ejecutar el circuito agente en cualquier entorno con consistencia.
# Uso: docker build -t ai-native-template . && docker run --rm -v $(pwd):/workdir ai-native-template
#================================================================================

FROM python:3.12-slim AS base

# Instalar PowerShell 7 (requerido para scripts .ps1 del circuito)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        ca-certificates \
        && rm -rf /var/lib/apt/lists/*

# Instalar PowerShell 7
RUN curl -fsSL https://aka.ms/install-powershell || true

# Configurar workdir
WORKDIR /workdir

# Copiar solo lo esencial para validación (no los runs/ ejemplos ajenos)
COPY --from=base . /workdir/

# Instalar dependencias Python
COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copiar resto de la estructura (excluyendo .git, runs/ ejemplos, node_modules)
COPY --chown=1000:1000 . .

# Excluir carpetas que no son necesarias en el container
RUN rm -rf /workdir/.git /workdir/node_modules /workdir/.pytest_cache /workdir/runs/00* /workdir/runs/01* /workdir/runs/02* /workdir/scripts/test_*

# Script entrypoint: validar template al entrar
ENTRYPOINT ["pwsh", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command"]

# Comandos por defecto al entrar al container
CMD ["-c", "Write-Host '=== Container AI-Native Template activo ===' -ForegroundColor Cyan && Write-Host 'Ejecute: pytest -v tests/' -ForegroundColor Gray && Write-Host 'O: pwsh -File .\\scripts\\sync-agentic-adapters.ps1 -Check' -ForegroundColor Gray"]

# Label metadata para consistencia y debug
LABEL org.ai-native.template="true" \
      org.ai-native.version="10.0.0" \
      org.ai-native.maintainer="template-maintainers" \
      com.github.actions.name="AI-Native Template" \
      com.github.actions.description="Template AI-Native con circuito agente completo"