Установка и запуск

1. Клонирование репозитория

 git clone 

2. Установка зависимостей

Если у вас не установлен Poetry, установите его

Активируйте виртуальное окружение и установите зависимости:

poetry shell
poetry install

3. Настройка переменных окружения

Создайте .env файл в корневой директории проекта и добавьте туда переменные из .env.example

4. Запуск проекта с Docker

Соберите и запустите контейнеры:

docker-compose up --build -d

Проверьте, что контейнеры работают:

docker ps

5. Доступ к API

После успешного запуска проекта API будет доступен по адресу:

http://127.0.0.1:8000/api/

Swagger UI:

http://127.0.0.1:8000/swagger/

6. Проверка Celery

Проверить, работают ли задачи Celery, можно через лог:

docker logs celery_worker --tail=50 -f

Пример ручного запуска задачи через Django shell:

docker exec -it django_app sh -c "python manage.py shell"
>>> from lms.tasks import send_course_update_email
>>> send_course_update_email.delay(42, ["user@example.com"])

Завершение работы

Чтобы остановить и удалить контейнеры, выполните:

docker-compose down
