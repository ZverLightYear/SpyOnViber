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
    "database": {
        "app_db": {
             "ENGINE": "postgresql+psycopg2",
             "USER": "sov_user",
             "PASSWORD": "sov_user",
             "HOST": "localhost",
             "DB_NAME": "sov_db"
        },
        "viber_db": {
            "ENGINE": "sqlite",
            "DB_NAME": "/home/user/.ViberPC/*******/viber.db"
        }
    }
}
```
`database` - содержит информацию о БД Viber `viber_db` и БД приложения `app_db`.

  * Для каждой БД задается набор параметров, необходимых для подключения к конкретной БД.
  * Обязательные поля: `ENGINE`, `DB_NAME`. 
  * Опциональные поля: `USER`, `PASSWORD`, `HOST`, `PORT`.
