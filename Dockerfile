FROM rasa/rasa:latest-spacy-en

# Copy model (this is required if you want to serve a trained model)
COPY ./models /app/models

# Copy everything else needed for Rasa
COPY ./data /app/data
COPY config.yml /app/
COPY domain.yml /app/
COPY credentials.yml /app/


# Set working directory
WORKDIR /app

# Start Rasa server with your trained model
CMD ["run", "--enable-api", "--debug", "--model", "models/latest.tar.gz"]
