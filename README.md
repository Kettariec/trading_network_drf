
<h2 align="center">Trading Network</h2>

Онлайн платформа торговой сети электроники.


<!-- USAGE EXAMPLES -->
## Usage

Перед запуском web-приложения создайте базу данных, создайте и примените миграции, установите необходимые пакеты из файла pyproject.toml и заполните файл .env по образцу .env.example. Используйте команду "python manage.py csu" для создания суперпользователя. Для запуска используйте команду "python manage.py runserver", либо через конфигурационные настройки PyCharm.


## Structure

config/

    settings.py - настройки приложений
    urls.py - файл маршрутизации

trading_network/

    migrations/
        папка с миграциями
    admin.py - настройки админки
    pagination.py - пагинация
    permissions.py - права доступа
    models.py - модели приложения
    serializers.py - сериализаторы
    tasks.py - отложенные и периодические задачи
    urls.py - файл маршрутизации приложения
    validatots.py - валидация
    views.py - контроллеры

user/
    
    avatar/
        папка с аватарами пользователей
    management/commands
        csu - кастомная команда создания суперпользователя
        create_user - создать юзера через терминал
    migrations/
        папка с миграциями
    admin.py - настройки админки
    serializers.py - сериализаторы
    models.py - модели приложения
    urls.py - файл маршрутизации приложения
    views.py - контроллеры

.env.example - образец заполнения переменных окружения.

manage.py - точка входа веб-приложения.

pyproject.toml - файл зависимостей проекта.

poetry.lock - файл Poetry.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact

kettariec@gmail.com

https://github.com/Kettariec/trading_network_drf/