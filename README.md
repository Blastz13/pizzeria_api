# Stack project

- **Python**
- **Django**
- **Django Rest Framework**
- **JWT**
- **PostgreSql**
- **Flake8**
- **PyTest**
- **Coverage**
- **Swagger**
- **Docker**
- **Docker-compose**

## Installation and launch

**Installation**

You can clone this application:

```bash 
git clone https://github.com/Blastz13/pizzeria_api.git
```

Next, you need to install the necessary libraries:

```bash
poetry install
poetry update
```
You need to set variables in the environment:

`POSTGRES_USER` — Database username

`POSTGRES_PASSWORD` — Database password

`POSTGRES_SERVER` — Database host

`POSTGRES_PORT` — Database port

`POSTGRES_DB` — Database name

`PGADMIN_DEFAULT_EMAIL` — Postgres admin email

`PGADMIN_DEFAULT_PASSWORD` — Postgres admin password

**Launch**

Change directory from web app, create and apply migrations:

```bash
cd pizzeria_api
python3 manage_dev.py collectstatic
python3 manage_dev.py makemigrations
python3 manage_dev.py migrate
```

Now you can start the server:

```bash
python3 manage_dev.py runserver
```

### License

Copyright © 2022 [Blastz13](https://github.com/Blastz13/).