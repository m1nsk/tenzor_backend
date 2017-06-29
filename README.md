#Instal virtualenv

```
./pip install virtualenv
./virtualenv env_tenzor

```

#Activate virtualenv

```
source env_tenzor/bin/activate

```

#Instal dependencies

```
./pip install -r requirements.txt

```

#Запуск

При первичном запуске произвести миграции

```
./python manage.py migrate
```

При первичном запуске следует создать суперпользователя

```
./python manage.py createsuperuser
```

Сам запуск

```
./python manage.py runserver
```
