# DinMo - Technical Assignment
***

## Table of Contents
1. [Introduction](#introduction)
2. [Technologies](#technologies)
3. [Project Setup](#project-setup)
4. [Testing](#testing)
5. [Deleting created images, containers, volumes](#deleting)
6. [Improvements](#improvements)


## __1. INTRODUCTION__
<a name="introduction"></a>

This project consists in a FastAPI backend application connected to a PostgreSQL DB. 

The DB contains one table named People having the following schema: 

id, name, age, gender, country, createdAt, updatedAt.

The FastAPI backend is made of three API endpoints:


* GET /api/people 

-> returns the average age of all the people (grouped by country) & the number of people from each country.

Example:
```
$ curl -X 'GET' \
  'http://localhost:8000/api/people/' \
  -H 'accept: application/json' \
  -H 'x-token: API_TOKEN'
```

* POST /api/people 

-> inserts a list of people to the DB.

Example:
```
$ curl -X 'POST' \
  'http://localhost:8000/api/people/' \
  -H 'accept: application/json' \
  -H 'x-token: API_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
  "people": [
    {
      "name": "Albert",
      "age": 40,
      "gender": "M",
      "country": "Germany"
    },
{
      "name": "Sophie",
      "age": 30,
      "gender": "F",
      "country": "France"
    }
  ]
}'
```
* GET /api/people/gender-repartition/{country} 

-> returns the gender repartition (male/female) for a given country.

Example:
```
$ curl -X 'GET' \
  'http://localhost:8000/api/people/gender-repartition/France' \
  -H 'accept: application/json' \
  -H 'x-token: API_TOKEN'
```

## __2. TECHNOLOGIES__
<a name="technologies"></a>

A list of technologies used within the project:
* [Docker](https://docs.docker.com/get-docker): Version 20.10.21
* [Docker-compose](https://docs.docker.com/compose/install): Version 2.13.0
* [Psql](https://www.postgresql.org/download/): Version 15.1
* [Fastapi](https://fastapi.tiangolo.com/): Version 0.88.0

Other used Python libraries are:
* Pytest: version 7.2.0
* Uvicorn version 0.20.0
* SQLAlchemy version 1.4.45
* Pydantic version 1.10.2
* Httpx version 0.23.1


### __3. PROJECT SETUP__
<a name="project-setup"></a>

Step 1 - Deploy the Postgres database container

```
$ docker-compose up -d
```

Step 2 - Install the dependencies in your virtual environment

```
$ pip3 install -r requirements.txt
```

Step 3 - Run the app

```
$ uvicorn app.main:app --host localhost --port 8000 --reload
```

 Step 4 (optional) - Connect to the DB to verify the inserted values in the table

```
$ psql postgres://postgres:password123@127.0.0.1:6500/fastapi
```

```
$ select * from People;
```

Once the Postgres db container is deployed and the app is running, you can go to  http://localhost:8000/docs to interact with the different API endpoints.
Please note that you need to add the following API Token in the headers: "TEST-API-TOKEN".



### __4. TESTING__
<a name="testing"></a>
For the moment only basic tests were added. These consist in testing that the different endpoints return the right response status code.

Please execute the following command to run the tests:
```
$ pytest
```

 ### __5. DELETING IMAGES, CONTAINERS, VOLUMES THAT WERE CREATED__
 <a name="deleting"></a>

When you are done with the project and want to stop the containers & delete the created images/volumes please run:

```
$ docker-compose down --volumes --rmi all
```

## __6. IMPROVEMENTS__
<a name="improvements"></a>

This project was a short mock-up. 
Please find the coming steps to improve it:
* Add unit tests for the API endpoints logic.
* Add proper authentication (OAuth2)
* Add constraint rules for the People table columns

    -> age between 0 and 150 

    -> Gender only F or M
    
    ...
* Dockerize the application