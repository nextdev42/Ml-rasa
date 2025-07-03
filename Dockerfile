FROM rasa/rasa:latest-spacy-en

COPY ./data /app/data
COPY ./models /app/models
COPY config.yml /app/config.yml
COPY domain.yml /app/domain.yml
COPY credentials.yml /app/credentials.yml
COPY endpoints.yml /app/endpoints.yml

WORKDIR /app

CMD ["run", "--enable-api", "--debug"]
