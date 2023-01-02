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

Step 1: Execute this command to run the postgres db container:

```
$ docker-compose up -d
```

Once the containers are running, you can go to  http://localhost:8000/docs to interact with the different api endpoints.
Please note that you need to add the following API Token in the headers: "TEST-API-TOKEN"


### __3. TESTING__
<a name="testing"></a>
For now only basic tests were added. These consist in testing that the different endpoints return the right response status code.

Please execute the following command to run the tests:
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