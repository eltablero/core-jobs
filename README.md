# core-bff
Core Backend For Frontend (BFF) del tablero. Es el punto de contacto con el frontend.

##  Pre-commit

Asegúrate de estar dentro del entorno de poetry

`poetry run pre-commit install`

Check

`poetry run pre-commit run --all-files`

## Run Tests

`poetry run pytest -v`

## Run app with `Colima`

`brew install docker`

`brew install colima`

`colima start`

`docker build . -t eltablero-core-jobs:latest`

`docker run -it -p 8000:8000 eltablero-core-jobs:latest`

## Project structure

```
core-jobs/
├── pyproject.toml           # Definición de dependencias (Poetry)
├── poetry.lock              # Versiones exactas de librerías
├── README.md
├── Dockerfile               # Configuración para Azure Container Apps
├── .dockerignore
├── src/                     # Código fuente
│   ├── __init__.py
│   ├── main.py              # PUNTO DE ENTRADA (Entrypoint para el Job)
│   ├── jobs/                # Definición de tareas específicas
│   │   ├── __init__.py
│   │   └── media_scraping.py
│   ├── core/                # Lógica de negocio pura (independiente de Azure)
│   │   ├── __init__.py
│   │   └── processor.py
│   └── infrastructure/      # Integraciones (Azure SDK, DBs, APIs)
│       ├── __init__.py
│       ├── blob_storage.py
│       └── database.py
└── tests/                   # Pruebas unitarias e integración
    ├── __init__.py
    └── test_jobs.py
```