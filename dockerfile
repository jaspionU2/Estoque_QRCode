FROM python:3.12

WORKDIR /Estoque_QRCode

COPY pyproject.toml /Estoque_QRCode/

RUN python3 -m venv .venv

RUN . .venv/bin/activate

RUN pip install poetry

RUN poetry install

RUN pip install sqlalchemy

RUN pip install pydantic-settings

RUN pip install --no-cache-dir "fastapi[standard]" uvicorn

COPY . /Estoque_QRCode

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000", "--reload"]