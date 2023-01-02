# DinMo - Technical Assignment
***

This project consists in a FastAPI backend connected to a PostgreSQL DB. The DB contains one table named People with the following schema: id, name, age, gender, country, createdAt, updatedAt.

The FastAPI backend is made of three API endpoints:

* POST /api/people -> inserts a list of people to the DB
* GET /api/people -> returns the average age of all the people (grouped by country) & the number of people from each country.
* GET /api/people/gender-repartition/{country} -> returns the gender repartition (male/female) for a given country


## Table of Contents
1. [Technologies](#technologies)
2. [Project Setup](#project-setup)
3. [Testing](#testing)
4. [Deleting created images, containers, volumes](#deleting)
5. [Improvements](#improvements)

## 1. Technologies
<a name="technologies"></a>

A list of technologies used within the project:
* [Docker](https://docs.docker.com/get-docker): Version 20.10.12
* [Docker-compose](https://docs.docker.com/compose/install): Version 1.29.2

The Python libraries used are:
* Pytest: version 7.0.1
* Uvicorn version 0.20.0

### __2. PROJECT SETUP__
<a name="project-setup"></a>

Step 1: Please run the following command to build the images contained in docker-compose.yaml:
```
$ docker-compose build
```

Step 2: Execute this command to run the corresponding containers:

```
$ docker-compose up -d
```

Once the containers are running, you can go to  http://localhost:8000/docs to interact with the backend.


### __3. TESTING__
<a name="testing"></a>
The functions used in the DAG were tested (tests can be found in *./tests/unit_tests*). 

The OSS Airflow project uses pytest, so the same was used in this project.

Before running the tests please install the required libs in your virtual environment by running the command:
```
$ pip install -r requirements.txt
```

Then copy the following command to run the tests:
```
$ pytest
```

 ### __4.DELETING IMAGES, CONTAINERS, VOLUMES THAT WERE CREATED__
 <a name="deleting"></a>

When you are done with the project and want to stop the containers & delete the created images/volumes please run:

```
$ docker-compose down --volumes --rmi all
```

## 5. IMPROVEMENTS
<a name="improvements"></a>

This project was a short mock-up. Please find the following steps to improve it:
* Implement the API endpoints logic testing.
* Add proper authentication (OAuth2 for example)