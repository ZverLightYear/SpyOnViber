# SpyOnViber
```
usage: spy_client.py 
```

Реализация на Python3.8
## Requirements:
  * sqlalchemy >= 1.4.15

## Пример конфигурационного файла conf.json:
```
{
    "databases": {
        "app_db": {
             "drivername": "postgresql+psycopg2",
             "username": "sov_user",
             "password": "sov_user",
             "host": "localhost",
             "port": "5432"
             "database": "sov_db"
        },
        "viber_db": {
            "drivername": "sqlite",
            "database": "/home/zver/.ViberPC/***********/viber.db"
        }
    }
}
```
`databases` - содержит информацию о БД Viber `viber_db` и БД приложения `app_db`.

  * Для каждой БД задается набор параметров, необходимых для подключения к конкретной БД.
  * Обязательные поля: `drivername`, `database`. 
  * Опциональные поля: `username`, `password`, `host`, `port`.
