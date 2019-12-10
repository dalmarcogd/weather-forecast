# Weather Forecast
Weather Forecast é um projeto que consulta previsões do tempo de forma assincrona.

### Tecnologias
Principais tecnologias utilizadas:
* [gunicorn] - Como http server para execução da api
* [gevent] - Classe de worker para Celery!
* [celery] - Geranciador de mesangens da filas
* [redis] - Redis para armazenamento de cache e como broker
* [alembic] - Para migração do banco de dados
* [SQLAlchemy] - ORM das entidades
* [pydantic] - Utilizado para validação dos payloads
* [fastapi] - Como web framework para construção de APIS

### Como executar

```sh
$ git clone https://github.com/dalmarcogd/weather-forecast.git
$ cd weather-forecast
$ docker-compose up
$ open http://localhost:8000/weather-forecast-api/docs
```

###Teste
Enviar uma requisição http para o endereço:
```
POST
/weather-forecast-api/v1/weather-forecasts
request:
{
    "cityName": "London"
}
ou 
{
    "latitude": 10
    "longitude": 10
}
response:
{
  "id": "95c1bca3-c9b7-4485-b890-eee8ad6eab7c"
}
```
Após realizar a chamada será respondido um UUID de consulta. 
Este deve ser realizado para realizar a proxima chamada:
```
GET
/weather-forecast-api/v1/weather-forecasts/95c1bca3-c9b7-4485-b890-eee8ad6eab7c
responde:
{
  "id": "95c1bca3-c9b7-4485-b890-eee8ad6eab7c",
  "status": "done",
  "result": {
    "coord": {
      "lon": 10,
      "lat": 10
    },
    "weather": [
      {
        "id": 804,
        "main": "Clouds",
        "description": "overcast clouds",
        "icon": "04d"
      }
    ],
    "base": "model",
    "main": {
      "temp": 305.29,
      "pressure": 1007,
      "humidity": 10,
      "temp_min": 305.29,
      "temp_max": 305.29,
      "sea_level": 1007,
      "grnd_level": 946
    },
    "wind": {
      "speed": 2.33,
      "deg": 51
    },
    "clouds": {
      "all": 88
    },
    "dt": 1575995400,
    "sys": {
      "country": "NG",
      "sunrise": 1575955569,
      "sunset": 1575997160
    },
    "timezone": 3600,
    "id": "95c1bca3-c9b7-4485-b890-eee8ad6eab7c",
    "name": "Birim",
    "cod": 200,
    "weatherForecastId": "95c1bca3-c9b7-4485-b890-eee8ad6eab7c"
  }
}
ou
{
  "id": "95c1bca3-c9b7-4485-b890-eee8ad6eab7c",
  "status": "process",
  "result": null
}
ou
{
  "id": "95c1bca3-c9b7-4485-b890-eee8ad6eab7c",
  "status": "error",
  "result": null
}
```


   [gunicorn]: <https://github.com/joemccann/dillinger.git>
   [gevent]: <https://github.com/gevent/gevent>
   [celery]: <http://daringfireball.net>
   [redis]: <https://pypi.org/project/redis/>
   [alembic]: <https://alembic.sqlalchemy.org/en/latest/>
   [SQLAlchemy]: <https://www.sqlalchemy.org/>
   [pydantic]: <https://pydantic-docs.helpmanual.io/>
   [fastapi]: <https://fastapi.tiangolo.com/>
   
   