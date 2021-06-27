FROM python:3.8

COPY . app/

ENV POETRY_VERSION=1.1.5

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR app

RUN poetry install

CMD poetry run streamlit run app.py --server.port 8502
