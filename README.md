# Тестовое задание отдел бэкенд Сафаран

## Задание состоит из двух директорий:

### Директория n_elements:

Решение задачи о n первых элементов последовательности. Функция принимает на вход
значение n числа элементов, вовзвращает последовательность 122333444455555... 
Число повторяется столько раз, чему оно равно.

### Директория food_shop:

Реализация проекта магазина продуктов.

Для запуска проекта локально c БД sqlite3:
1) В корневом каталоге создать .env файл
2) Описать переменные:
  * SECRET_KEY="'<ваш SECRET_KEY>'"

Например SECRET_KET="'django-insecure-k21i13@3f^h'"
  * ALLOWED_HOSTS="'<ваши ALLLOWED_HOSTS>'"'

Например ALLOWED_HOSTS="'localhost,web,127.0.0.1''"
```
cd food_shop
python3 manage.py runserver
```

Для запуска в Docker-контейнере с БД PostgreSQL:
1) В корневом каталоге создать .env файл
2) Описать переменные:
  * SECRET_KEY=<>
  * ALLOWED_HOSTS=<>
  * ENGINE=<>
  * POSTGRES_DB=<>
  * POSTGRES_USER=<>
  * POSTGRES_PASSWORD=<>
  * DB_NAME=<>
  * DB_HOST=<>
  * DB_PORT=<>

Реализована авторизация пользователя 
с применение Djoser.

Значения Суперюзера для проверки админ-зоны:

- Электронная почта: admin@admin.com
- Username: admin_username
- Пароль: admin_password 
- Имя пользователя: admin 
- Фамилия: admin

Технологии
```
Python 3.10
Django 4.2
Django REST framework 3.14.0
Djoser 2.2.2
Postgres
```

Автор
- [Виталий Черемисов](https://github.com/VitaliiCheremisov)