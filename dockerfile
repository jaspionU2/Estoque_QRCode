FROM python

WORKDIR /Estoque_QRCode

COPY pyproject.toml /Estoque_QRCode/

RUN python3 -m venv .venv

RUN pip install poetry

RUN poetry install

RUN pip install --no-cache-dir "fastapi[standard]" uvicorn

RUN . .venv/bin/activate

COPY . /Estoque_QRCode

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000", "--reload"]