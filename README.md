# Airflow Multi-Environment Template

This project provides a ready-to-use multi-environment setup for Apache Airflow using Docker Compose.

## Environments

- **Local Development** (`docker-compose.local.yaml` + `.env.local`)
- **Staging on EC2** (`docker-compose.stage.yaml` + `.env.stage`)
- **Production on EC2** (`docker-compose.prod.yaml` + `.env.prod`)

## Setup Instructions

1. Generate your Fernet and Webserver Secret Keys:
    ```bash
    python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
    python -c "import secrets; print(secrets.token_hex(16))"
    ```
    Add them to the appropriate `.env` files.

2. Run locally:
    ```bash
    docker-compose --env-file .env.local -f docker-compose.local.yaml up -d
    ```

3. Run on EC2 for staging:
    ```bash
    docker-compose --env-file .env.stage -f docker-compose.stage.yaml up -d
    ```

4. First-time user creation (run inside the webserver container):
    ```bash
    docker-compose exec airflow-webserver airflow users create \
        --username admin \
        --password admin \
        --firstname Air \
        --lastname Flow \
        --role Admin \
        --email admin@example.com
    ```

## Folder Structure

```
airflow-multi-env-template/
├── dags/                                # Your DAG scripts
├── plugins/                             # Custom plugins (if any)
├── logs/                                # Airflow logs (mounted for persistence)
├── docker-compose.local.yaml            # Local Docker Compose
├── docker-compose.stage.yaml            # Staging Docker Compose
├── docker-compose.prod.yaml             # Production Docker Compose
├── .env.local                           # Local environment variables
├── .env.stage                           # Staging environment variables
├── .env.prod                            # Production environment variables
├── README.md                            # Full documentation
└── .gitignore                           # Ignores unnecessary files
```

---
    