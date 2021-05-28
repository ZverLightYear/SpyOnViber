# SpyOnViber
```
usage: spy_client.py 
```

Реализация на Python3.8


## Requirements:
  * sqlalchemy >= 1.4.15
  * termcolor >= 1.1.0
  * psycopg2 >= 2.8.6


## Quick Start:

Перед запуском необходимо:
  * Установить Desktop версию Viber (https://www.viber.com/ru/download/) + авторизовать в нем учетную запись.
  * Для работы с БД приложения установить БД (Любую. В проекте используется PostgreSQL).
    * Создать БД.
    * Создать пользователя с правами записи в эту БД.
  * Внести все необходимые данные в файл конфигурации приложения.  

### Example using PostgreSQL

Установка драйвера psycopg2:
```shell
pip install psycopg2
```

Установка PostgreSQL:
```shell
sudo apt update
sudo apt install postgresql postgresql-contrib
```

Зайти в админку PostgreSQL:
```shell
sudo -u postgres psql
```

Создать пользователя для работы с БД:
```
CREATE USER sov_user WITH PASSWORD 'sov_user';
```

Создать БД и назначить права на ее использование:
```
CREATE DATABASE sov_db OWNER sov_user;
GRANT ALL PRIVILEGES ON DATABASE "sov_db" to sov_user;
```

[Опционально] Внести нужные правки в конфигурационный файл PostgreSQL.
Местоположение файла конфигурации узнаем командой: 
```
SHOW config_file;

----------------------------------------- 
/var/lib/pgsql/9.6/data/postgresql.conf
(1 row)
```

По умолчанию для работы с PostgreSQL используется порт `5432`

## Пример конфигурационного файла conf.json:
```json
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
            "database": "/home/user/.ViberPC/***********/viber.db"
        }
    }
    "settings": {
        "logging": {
            "level": "DEBUG"
        },
        "process_sleep_time": 5
    }    
}
```

`databases` - содержит информацию о БД Viber `viber_db` и БД приложения `app_db`.

  * Для каждой БД задается набор параметров, необходимых для подключения к конкретной БД.
  * Обязательные поля: 
    * `drivername` - драйвер подключения к базе данных.
    * `database` - имя базы данных. Файл БД Viber располагается:
      * для Linux `~/.ViberPC/<phone_number>/viber.db`
      * для Windows `C:\Users\<user>\AppData\Roaming\ViberPC\<phone_number>\viber.db`
  * Опциональные поля: `username`, `password`, `host`, `port`.

`settings` - хранит настройки клиента сбора сообщений.
  * `process_sleep_time` - таймаут сбора новых сообщений.
  * `logging` - настройки логирования сообщений. 
    * `level` - `DEBUG` включает логирование. Все остальное выключает =)