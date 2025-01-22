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

### < Migrations >

#### - Gerar o arquivo de migration do Alembic -

`alembic revision --autogenerate -m <adicionar comentario sobre migration(opcional)>`

#### - Subir migration para o DB -

`alembic upgrade head` ou passar o id da revision criada, identificado no arquivo como **Revision ID** `alembic upgrade <Revision ID da migration>`

Caso queira, passe a quantidade de migrations que deseja subir para o banco com Ex. `alembic upgrade 2`

#### - Desfazer migration do DB -

`alembic downgrade head` ou passar o id da revision criada, identificado no arquivo como **Revision ID** `alembic downgrade <Revision ID da migration>`

Caso queira, passe a quantidade de migrations que deseja desfazer no banco com Ex. `alembic upgrade 2`
