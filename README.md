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