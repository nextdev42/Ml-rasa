# Ml‑rasa

A Docker‑ized Rasa chatbot project, with SPAcy NLP, ready for local development (Gitpod/Codespaces) and deployment (Railway).



## 📂 Project Structure

```bash
├── config.yml
├── credentials.yml
├── data/
│ ├── nlu.yml
│ ├── stories.yml
│ └── rules.yml
├── domain.yml
├── docker-compose.yml
├── Dockerfile
├── endpoints.yml
├── models/
│ └── latest.tar.gz
└── README.md
```

## 🚀 Quickstart

### 1. Clone

```bash
git clone https://github.com/nextdev42/Ml-rasa.git
cd Ml-rasa
```
### 2. Local Dev with Docker Compose (Gitpod/Codespaces or Local)
```bash
docker compose build
docker compose up
```

Rasa REST API available at
```bash http://localhost:5005```

To train a new model:
```bash
docker compose run --rm rasa rasa train \
  --output models --fixed-model-name latest
```

### 3. Direct CLI (inside container)
```bash
docker compose run --rm rasa bash
# then inside container shell:
rasa train
exit
```

### 📦 Deployment on Railway

1. Ensure ```models/latest.tar.gz``` is committed.

2. Push to GitHub.

3. Link your repo in Railway (will auto‑detect ```Dockerfile``` ).

4. Expose port **5005** in Railway settings.

5. Railway will build and run your container:
   
```bash
CMD ["run","--enable-api","--debug","--model","models/latest.tar.gz"]
```
Your bot will be live at:
```bash
https://<your-railway-app>.up.railway.app
```

### 🛠 Configuration Files

**config.yml** — NLU pipeline & policies

**domain.yml** — Intents, entities, responses

**credentials.yml** — ```rest:``` (only REST enabled)

**endpoints.yml** — (empty / commented until using actions)

### 📚 Useful Commands

| Task        | Command                                                                             |
| ----------- | ----------------------------------------------------------------------------------- |
| Train Model | `docker compose run --rm rasa rasa train --output models --fixed-model-name latest` |
| Shell Chat  | `docker compose run --rm rasa rasa shell --debug`                                   |
| Run Server  | `docker compose up`                                                                 |
| Copy Model  | `docker cp <container>:/app/models/latest.tar.gz ./models/latest.tar.gz`            |

### 👤 Author
Nextdev42 — Tanzanian developer

📫 GitHub
