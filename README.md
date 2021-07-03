
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
├── app
│   ├── core
│   │   ├── config.py
│   │   ├── dataimp.py
│   │   ├── exceptions.py
│   │   └── utils.py
│   ├── database.py
│   ├── __init__.py
│   ├── repository
│   │   └─ provider.py
│   ├── routers
│   │   └── provider.py
│   └── schemas.py
├── generate_data.py
└── main.py
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