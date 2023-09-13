# Create a REST API

The second task for HNG Internship is to develop a REST API with Basic CRUD Operation.

## Tech Stack

**Framework:** FastAPI

**Databases:**
SQLite (local), Postgres (production)

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

## Sample

To view a detailed **Request and Response** format, click [here](https://personapi.up.railway.app/redoc).

```JSON
{
  "name": "pele soccer",
  "user_id": 7
}
```

## Running Tests

A test file "sql_test.py" has been created with tests to check.
To run tests, run the following command

```bash
  pytest
```

## More on documentation

Check out a live interactive documentation [here](https://personapi.up.railway.app/docs). It will allow interact/test the API with ease.

## Demo

This is a demo on how to go about interacting with the API.

## Deployment

This API is deployed on Railway. Locally the database used is SQLite while for production it's PostgreSQL.

psycopg2-binary was installed due to the production database.

## Appendix

The "person.db" database should be deleted, if you named your database some different from "person".
