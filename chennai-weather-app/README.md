# Chennai Weather App

A minimal frontend + FastAPI backend for a DevOps deployment practice project.

## Architecture

Browser -> Nginx frontend container -> FastAPI backend container -> Open-Meteo API

## Run locally with Docker Compose

Prerequisites: Docker Engine/Desktop with the Compose plugin.

From this project directory:

```bash
docker compose up --build -d
```

Open http://localhost:8080 and click **Get Chennai Weather**.

Check the backend health endpoint:

```bash
curl http://localhost:8080/api/health
```

View logs:

```bash
docker compose logs -f
```

Stop the app:

```bash
docker compose down
```

## API endpoints

- `GET /api/health` — health check
- `GET /api/weather` — current weather for Chennai

The backend calls Open-Meteo, so an internet connection is required from the backend container. No API key is needed for this basic demo.

## DevOps project plan

- Terraform: provision EC2 and its security group.
- Ansible: install Docker and configure the host.
- GitHub Actions: test/build images, publish them to a container registry, and deploy to EC2.
- Never commit SSH private keys, cloud credentials, or Terraform state.
