
# Create a REST API

The second task for HNG Internship is to develop a REST API with Basic CRUD Operation.

## Tech Stack

**Framework:** FastAPI

**Server:** uvicorn

**Databases:**
SQLite (local), PostgreSQL (production)

## Run Locally

If you choose to **fork** before cloning the project be sure to **use the link from your own repo to clone**.

Clone the project

```bash
  git clone https://github.com/A3AJAGBE/person_api
```

Go to the project directory

```bash
  cd person_api
```

Create virtual environment

```bash
  python3 -m venv venv
```

Activate virtual environment

```bash
  source venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  uvicorn main:app --reload
```

## Environment Variables

To run this project, you will need to create a .env file and add the environment variable to it.

`DATABASE_URL`

an example on how to set the variable

```
DATABASE_URL = "sqlite:///[INSERT DB NAME HERE].db"
```

## API Reference

#### POST the data

```https
POST /api
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | **Required**|

#### GET all the data

```https
GET /
```

#### GET the data by id

```https
GET /api/{user_id}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `integer` | **Required**|

#### GET the data by using name

```https
GET /api?name=[INSERT HERE]
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | **Required**|

#### PUT the data by id

```https
PUT /api/{user_id}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `integer` | **Required**|

#### DELETE the data by id

```https
DELETE /api/{user_id}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `integer` | **Required**|

## Running Tests

A test file "sql_test.py" has been created with tests to check.
To run tests, run the following command

```bash
  pytest
```

## Deployment

This API is deployed on Railway. Locally the database used is SQLite while for production it's PostgreSQL.

psycopg2-binary was installed due to the production database.

## Limitations/Assumptions

- Familiarity  with Python
- Familiarity  with git and GitHub
- No auth Implementation for the API
- The application was developed on  MacOS
- Knowledge of using the command line interface (CLI)

## Appendix

The "person.db" database should be deleted, if you named or wish to name your database some different from "person".

If you are using a different device, lookup on how certain things are done. e.g creating a virtual environment.
