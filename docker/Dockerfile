FROM python:3.8

COPY . app/

ENV POETRY_VERSION=1.1.5

# RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR app

RUN poetry install

CMD poetry run streamlit run app.py --server.port 8502
# CMD ["poetry", "run", "streamlit", "run", "app.py"]
