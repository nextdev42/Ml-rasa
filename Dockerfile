FROM rasa/rasa:latest-spacy-en

# Copy your project into the image
COPY ./data /app/data
COPY ./models /app/models
COPY config.yml /app/config.yml
COPY domain.yml /app/domain.yml
COPY credentials.yml /app/credentials.yml
COPY endpoints.yml /app/endpoints.yml

WORKDIR /app

# Expose the port Railway will use
EXPOSE 5005

# Start Rasa and point at your trained model
CMD ["run", "--enable-api", "--debug", "--model", "models/latest.tar.gz"]
