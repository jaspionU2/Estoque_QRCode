# Dependências 

- fastapi: __^0.115.5__
- uvicorn: __^0.32.0"__
- psycopg2-binary: __^2.9.5__
- python-dotenv: __^1.0.1__
- sqlalchemy: __^2.0.36__
- alembic: __^1.14.0__
- pydantic-settings: __^2.6.1__
- psycopg2: __^2.9.10__
- pyjwt: __^2.10.1__
- pwdlib: __^0.2.1__

# Lista de comandos

### < Entrar no ambiente virtual >

`source .venv/bin/activate`

### < Baixar todas das dependências >

`poetry updade`

### < Adicionar uma nova dependência >

`poetry add <nome-dependência>`

### < Executar o projeto >

`fastapi dev main.py`

### < Testes >
#### - Controller -

`pytest --cov=controller`

#### - Service -

`pytest --cov=service`

#### - Gerar um html com mais detalhes relacionados aos testes -

`coverage html`
