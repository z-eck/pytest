FROM python:3.12-slim

WORKDIR /app

COPY ./pyproject.toml ./

RUN pip install poetry && poetry install

COPY ./docs ./docs

COPY ./mkdocs.yml ./

COPY ./exclude.sh ./
RUN chmod +x exclude.sh && ./exclude.sh

COPY ./libs ./

EXPOSE 8000

CMD ["poetry", "run", "mkdocs", "serve", "-a", "0.0.0.0:8000"]
