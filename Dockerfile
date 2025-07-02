FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    libjpeg-dev \
    zlib1g-dev \
    git \
    curl \
    libyaml-dev \
    python3-dev \
 && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --upgrade pip setuptools wheel
RUN pip install --only-binary :all: pyyaml==5.4.1
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_md

RUN rasa train

CMD ["rasa", "run", "--enable-api", "--cors", "*", "--port", "8000"]
