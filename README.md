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

   [gunicorn]: <https://github.com/joemccann/dillinger.git>
   [gevent]: <https://github.com/gevent/gevent>
   [celery]: <http://daringfireball.net>
   [redis]: <https://pypi.org/project/redis/>
   [alembic]: <https://alembic.sqlalchemy.org/en/latest/>
   [SQLAlchemy]: <https://www.sqlalchemy.org/>
   [pydantic]: <https://pydantic-docs.helpmanual.io/>
   [fastapi]: <https://fastapi.tiangolo.com/>
   
   