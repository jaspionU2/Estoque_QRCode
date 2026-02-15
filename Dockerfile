FROM python:3.12-slim

WORKDIR /app

# Instalar dependências do sistema para o psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Instalar Poetry
RUN pip install poetry

# Configurar Poetry para não criar ambientes virtuais dentro do container
RUN poetry config virtualenvs.create false

# Copiar apenas arquivos de dependência primeiro
COPY pyproject.toml poetry.lock* /app/

# Tentar instalar dependências
RUN poetry install --no-interaction --no-ansi --no-root

# Copiar o resto do código
COPY . /app

EXPOSE 8000

# Usar 0.0.0.0 para permitir conexões externas ao container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
