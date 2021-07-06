# quick-service
An app that allows customers to create service requests



## Description
The **fquick-service app** is an application that allows customers to create service requests. The project is divided into two parts. The Frontend build on **React - Javascript** and the Backend built on **Flask - Python**.


- Key Application features
    - Creating a service request order
    - Listing all orders
    - Search service requests by service id
    - Search service requests by date range
	- Admin panel to add data to db(dev)

- Contraints
    - Service requests can not be created on holidays
    - Service requests can not be created on sundays
    - Service requests can only be created mon-sat 9am-5pm
	- service requests cannot be creeated on a date/time where another request already exists(Time slot must be free)

## Technology Stack

- Flask
- DReact
- Postgres
- Docker
- Pytest

## Set Up Development With Docker(Recommended)- Backend

To setup for development with Docker after cloning the repository please do/run the following commands in the order stated below:

-   `cd <project dir>` to check into the dir
-   `docker-compose build`

Note : Depending on your system you might need to run `chmod +x entrypoint.sh` before building to enable copy the entrypoint.sh file over to docker
-   `docker-compose up -d` to start the api after the previous command is successful

The `docker-compose build` command builds the docker image where the api and its postgres database would be situated.
Also this command does the necessary setup that is needed for the API to connect to the database.

Run `docker-compose exec api python manage.py recreate_db` to create database
Run  `docker-compose exec api python manage.py seed_db` to seed db 

RUN `docker-compose exec api python -m pytest "src/tests"` To run test


API route will be live at `http://127.0.0.1:5000/`

ADMIN ROUTE `http://127.0.0.1:5000/admin`


SWAGGER DOCS ROUTE `http://127.0.0.1:5000/`


To stop the running containers run the command `docker-compose down`

###  Setting Up For Local Development(Backend)

-   Check that python 3 is installed:

    ```
    python --version
    >> Python 3.7.0
    ```

-   Clone the favorite-thing repo and cd into it:

    ```
    git clone https://github.com/tonyguesswho/quick-service.git
    ```
- activate a virtual enviroment

-   Install dependencies from requirements.txt file:

    ```
    pip install -r requirements.txt
    ```

-   Make a copy of the .env.sample file in the app folder and rename it to .env and update the variables accordingly:

    ```
		export FLASK_ENV=development
		export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/ser
		export DATABASE_TEST_URL=postgresql://postgres:postgres@localhost:5432/ser_test

    ```

- To reacreate db run `python manage.py recreate_db`
- To seed db run `python manage.py seed_db`
- To run test `python -m pytest "src/tests"`
- Run the server with `python manage.py run`






## API Endpoints
<table>
  <tr>
      <th>Request</th>
      <th>End Point</th>
      <th>Action</th>
  </tr>
    <tr>
      <td>POST</td>
      <td>/orders</td>
      <td>Create order</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/orders</td>
    <td>Get all orders</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/services/</td>
    <td>Get all services</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/orders?service_id=1</td>
    <td>Search orders by service id</td>
  </tr>
 <tr>
    <td>GET</td>
    <td>/orders?start_date=2000-11-10T09:10:21.524485Z&end_date=2041-11-10T09:10:21.524485Z</td>
    <td>Search orders by date range</td>
  </tr>
</table>



FROM node:16-alpine

# set working directory
WORKDIR /usr/src/app

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY ./package.json .
COPY ./yarn.lock .
COPY ./src .
COPY ./public .
RUN yarn install

CMD ["yarn", "start"]



/////

node_modules