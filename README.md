
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

## Request and Response Format

#### Create a person (POST)

##### Request Format

```JSON
{
  "name": "joel d'souza"
}
```

##### Response Format (success 200)

```JSON
{
  "name": "Joel D'Souza",
  "user_id": 1
}
```

##### Response Format (Bad Request - 400)

```JSON
{
  "detail": "Name exist already"
}
```

##### Request Format

```JSON
{
  "name": "JaneDoe-Smith"
}
```

##### Response Format (Bad Request - 400)

```JSON
{
  "detail": "Ensure there's space between first and last name. Apostrophe and hyphen allowed"
}
```

#### Get a person by id (GET)

##### Response Format (success 200)

```JSON
{
  "name": "Joel D'Souza",
  "user_id": 1
}
```

##### Response Format (Not Found - 404)

```JSON
{
  "detail": "Person not found"
}
```

#### Get a person using name (GET)

##### Response Format (success 200)

```JSON
{
  "name": "Joel D'Souza",
  "user_id": 1
}
```

##### Response Format (Not Found - 404)

```JSON
{
  "detail": "Person not found"
}
```

#### Update a person (PUT)

##### Request Format

```JSON
{
  "name": "darnarys fire"
}
```

##### Response Format (success 200)

```JSON
{
  "name": "Darnarys Fire",
  "user_id": 1
}
```

##### Response Format (Bad Request - 400)

```JSON
{
  "detail": "No change in the name"
}
```

##### Response Format (Bad Request - 400)

```JSON
{
  "detail": "Name exist already"
}
```

##### Request Format

```JSON
{
  "name": "DarnarysFire"
}
```

##### Response Format (Bad Request - 400)

```JSON
{
  "detail": "Ensure there's space between first and last name. Apostrophe and hyphen allowed"
}
```

##### Response Format (Not Found - 404)

```JSON
{
  "detail": "Person not found"
}
```

#### Delete a person (DELETE)

##### Response Format (success 200)

```JSON
"Person with id number: 1 was deleted."
```

##### Response Format (Not Found - 404)

```JSON
{
  "detail": "Person with id number: 3, not found."
}
```

## Sample API Usage

#### Create a person

``` Python
import requests

api_url = "http://127.0.0.1:8000/api"

add_person = {
    "name": "jessica pier"
}

res = requests.post(api_url, json=add_person)
data = res.json()
print(data)
```

#### Read a person by id

``` Python
import requests

api_url = "http://127.0.0.1:8000/api/19"

res = requests.get(api_url)
data = res.json()
print(data)
```

#### Read a person using name

``` Python
import requests

api_url = "http://127.0.0.1:8000/api?name=jessica pier"

res = requests.get(api_url)
data = res.json()
print(data)
```

#### Update a person

``` Python
import requests

api_url = "http://127.0.0.1:8000/api/19"

update_person = {
    "name": "jess pier"
}

res = requests.put(api_url, json=update_person)
data = res.json()
print(data)
```

#### Delete a person

``` Python
import requests

api_url = "http://127.0.0.1:8000/api/19"

res = requests.delete(api_url)
data = res.json()
print(data)
```

## Running Tests

A test file "sql_test.py" has been created with tests to check.
To run tests, run the following command

```bash
  pytest
```

## More on documentation

Check out a live interactive documentation [here](https://personapi.up.railway.app/api/livedocumentation). It will allow you interact/test the API with ease.

- Go to the page
- Click on the dropdown button on the right side corner of each requests (POST, GET, PUT, DELETE)
- Click on "Try it now" button, it's on the right side corner as well
- Fill the request body (if any)
- click on "Execute"

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
