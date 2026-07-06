# 3-tier app

![CI](https://github.com/Hellinor/3tier-app/actions/workflows/ci.yml/badge.svg)

A containerized 3-tier web application built with Docker Compose. It serves a visit
counter that shows a web frontend, a backend API, and a database working together.

## architecture

```
browser  -->  web (nginx, port 8000)  -->  api (Flask)  -->  db (postgres)
```

- **web** — nginx serving the UI and acting as a reverse proxy to the api. The only
  service exposed to the outside world (port 8000).
- **api** — a Flask app that connects to the database and returns a visit counter as JSON.
- **db** — a postgres database with a named volume for persistence. Stays private inside
  the network.

The three services find each other by name over a Docker Compose network. Only the web
tier is published; the api and db stay hidden.

## how to run

```bash
docker compose up -d --build
```

Then open http://localhost:8000 — each refresh increments the counter, proving the full
browser → web → api → db flow.

To stop everything:

```bash
docker compose down
```

## tech used

- Docker & Docker Compose
- nginx (reverse proxy)
- Python / Flask
- PostgreSQL
