# Healthcare Provider Directory APP

Individual parts of projects are on follwing branches  
`part_1`  
`part_2`  
`part_3`

## Generate mock data

```
mkdir database
python generate_data.py   # generates 300 records in pickle format
```

## Structure

```
├── app                     # fastapi app
│   ├── __init__.py         #
│   ├── core                #
│   │   ├── config.py       # setting and configurations
│   │   ├── dataimp.py      # file database implimentation
│   │   ├── exceptions.py   # exceptions used
│   │   └── utils.py        # utils
│   ├── database.py         # database
│   ├── repository          #
│   │   └─ provider.py      # providers data access
│   ├── routers             #
│   │   └── provider.py     # providers routes
│   ├── schemas.py          # pydantic schemas
│   └── main.py             # entry to fastapi app
└── generate_data.py        # mock data generator
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/mgautam98/fastapi-hpd.git
```

Go to the project directory

```bash
  cd fastapi-hpd
```

Install dependencies, requires `poetry`

```bash
  poetry install
```

Start the server

```bash
  uvicorn app.main:app --reload
```

## Deployment

To deploy this project run

```bash
  docker-compose up
```

## Running Tests

To run tests, run the following command

```bash
  pytest
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`POSTGRES_URL`  
`POSTGRES_USER`  
`POSTGRES_PW`

## Screenshots

<p align="center">
  <img src="https://i.imgur.com/Ie4yHj7.png" alt="Mailsy" width="900"/>
  <img src="https://i.imgur.com/b62TRtY.png" alt="Mailsy" width="900"/>
  <img src="https://i.imgur.com/rqmyNZ2.png" alt="Mailsy" width="900"/>
  <img src="https://i.imgur.com/eH3KXXt.png" alt="Mailsy" width="900"/>
</p>

<!--
## API Reference

#### Get all providers

```http
  GET /api/provider
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `skip` | `int` | Number of records to skip |
| `limit` | `int` | Number of records to get |

#### Get provider

```http
  GET /api/provider/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `UUID` | **Required**. Id of item to fetch |
 -->

<!-- Run Sonarqube -->

<!--
sonar-scanner \
  -Dsonar.projectKey=python-project \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=7656e444cbd8a437332d6cf1d9bc3176819368bb
 -->
