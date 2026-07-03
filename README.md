# Bookish

This is an exercise to help people practice APIs and DB interactions using Docker and FastAPI.

It uses the following tools for dependency and migrations management. These can be treated as a black box for the time being, as they are not the primary purpose of the exercise:
- [poetry](https://python-poetry.org/) is a dependency manager that creates a virtual Python environment. For now, all you need to know is that you should append `poetry run` before the commands you would normally run to interact with Python in your terminal
- [alembic](https://alembic.sqlalchemy.org/en/latest/) is a database migration tool, which allows us to automatically generate a database state based on the existing SQLAlchemy classes (more in the [Project Structure](#project-structure) section)

## Set-up

- Open `Docker Desktop` and make sure the engine is running.
- Create a `.env` file based on `.env-template` and set your DB parameters.
- Run `docker compose up` in a terminal in the main directory of the project. This uses `docker-compose.yml` to create the necessary containers.
- Go to `Docker Desktop` and search for the `bookish_api` container
- After you create new models and schemas for your tables, go to the `Exec` tab and run `poetry run alembic revision --autogenerate -m "<message>"` to generate the corresponding migration. Then, run `poetry run alembic upgrade head` to apply the migration. You can also do these steps at the beginning to generate the `Test` table.
- Go to the `bookish_db` container, in the `Exec` tab and run `psql -d <db_name> -U <username> -W `. You will be prompted to type in the password you added to `.env`. This will log you into the PostgreSQL server. From there, you should see the name of your DB that you set up in `.env` as a prefix in your terminal. Run `\dt` to see all available tables

You should now create new tables for your 21st century library!

## Project Structure

There are 2 folders, `api` and `db`. The `db` folder is only there for the `docker` container to use for generated data, you won't have to interact with it directly.

Structure of `api`:
- `/app` is where most of your work will actually be done:
    - `/controllers` contains the routers. This is where you define what endpoints your API has
    - `/helpers` contains useful scripts for interacting with the database
    - `/models` contains the [SQLAlchemy](https://www.sqlalchemy.org/) classes we will define. Here we define the structure of the SQL tables by using Python classes
    - `/schemas` are similar to `models`, but they represent the classes that we use for API interaction. [Pydantic](https://www.geeksforgeeks.org/python/introduction-to-python-pydantic-library/) allows us to create classes from the `BaseModel` and validate requests coming into the API or results that we return
    - `main.py` is where we define our `FastAPI` app. You should include all future routers/ controllers here
- `/migrations` contains the code we use through `alembic` to generate and run our migrations. Did you notice anything changing after you run the alembic commands in the set-up?