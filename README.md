Написать веб-приложение заходя на главную страницу которого пользователь видит
текущий курс рубля для доллара и евро. Источник получения курса валюты можно
выбрать на свое усмотрение. Курс необходимо обновлять раз в сутки. Пользователь
может выбрать день (сегодня, вчера, позавчера) и увидеть курс на этот день. В
приложении должны присутствовать unit-тесты на вывод курса и его
получение/обновление.

User-story:
1. Пользователь заходит на сайт
2. Пользователь видит текущий курс рубля для доллара и евро.
3. Пользователь выбирает день, видит курс на этот день.

Backend:
1. Веб-сервер обрабатывает запрос, отдает страницу
2. Со страницы выполняется запрос на бэк, берутся текущие данные по курсам.
3. Пользователь меняет дату на странице и запрашивает то же что ив предыдщуем шаге.

Как получать валюту?
1. Celery-задачи раз в сутки
2. Крон-задачи для получения данных и хранения в БД