# Job Directory

### *Job Directory* - это веб-приложение, которое представляет собой каталог вакансий. Это приложение разработано на языке программирования Python с использованием фреймворка Django. Оно позволяет пользователям просматривать список доступных вакансий и добавлять новые.

## Установка и запуск

### Перед началом работы:

В корневой папке находиться файл с зависимостями requirements.txt
```shell
pip install -r requirements.txt
```

### Развертывание базы данных:

Для удобства развертывания базы данных в папке database находиться файл docker-compose 

```shell
cd /database
docker-compose up -d 
```

loaddata.json файл для заполнения базы данных

```shell
pyhon ./manage.py loaddata ./database/loaddata.json
```
