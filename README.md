# Recipe app API

**Привет!**

В данном курсе вы научитесь работать с Django и его экосистемой. Курс лучше читать по коммитам, ниже увидите список
коммитов от первого до завершающего, к каждому коммиту в данном readme будет описание того что происходит. Для комфорта
советую работать на **~~ОС Linux~~** и в среде разработки **_PyCharm CE_**.

_P.S. если что не ясно пишите мне в телегу @temirlan100, но сперва ГУГЛИТЕ! =)_

Как полностью поймете все коммиты, сделаете ДЗ:

* Дополните новые API (сперва тесты, затем функционал)
* Прикрутите front к проекту на выбор (Vue, React, Angular)

**Этот курс прокачает скиллы:**

* Django
* Django Rest Framework
* Travis CI
* TDD
* Docker
* PostgreSQL

# Commit #1

Создайте открытый репозиторий в `github` с названием **_recipe-app-api_**. При создании репозитория `github` предложит
добавить файлы
`readme`, `.gitignore`, `license`, стоит обратить внимание на
`.gitignore` выберите язык Python и многие вещи с вашей локальной репы не будут лететь в `github` и это генерится
автоматом. Если вы работаете через `PyCharm` стоит так же добавить `.idea `
в `.gitignore`

[Инициализация репозитория Click!](https://github.com/temirlan100/recipe-app-api/commit/6ada73ffc8782265fb4350ea84b6bf0c86464aa4)

# Commit #2

В этом коммите не нужно все копировать к себе, достаточно
`Dockerfile` `docker-compose.yml` `requirements.txt` остальные файлы можно создать внутри контейнера так как это самые
стартовые файлы Django и далее эти файлы появятся у вас в среде разработки.

Прежде чем делать посмотрите внимательно на `Dockerfile` и что именно он содержит. Давайте сперва попробуем собрать наш
контейнер с помощью команды
`docker build .`, если все прошло успешно то в конце будет такой текст _**Successfully built container_id**_, если
возникла ошибка внимательно посмотрите на каком шаге, возможно в контейнере нет папки `app` или файла `requirements.txt`
.

Теперь давайте попробуем собрать контейнер через `docker-compose.yml`
файл с помощью команды `docker-compose build` если все прошло успешно то в конце будет такой текст

_**Successfully built container_id**_

_**Successfully tagged recipe-app-api:latest**_

Стоп в `docker-compose.yml` есть команда
`sh -c "python manage.py runserver 0.0.0.0:8000"` которая запускает приложение Django, а саму штангу мы не
инициализировали, а только поставили нужные зависимости. Давайте исправим! Наберите команду в терминале
`docker-compose run app sh -c "django-admin.py startproject app ."`
и если все прошло ок, тогда вы увидите файлы в папке app которая по умолчанию формирует Django.

Так же попробуйте открыть свое приложение через браузер по адресу
http://localhost:8000, сперва набрав команду
`docker-compose up -d`.

[Стартуем штангу через докер Click!](https://github.com/temirlan100/recipe-app-api/commit/15922c1cd6c749fc2bec5b7f7de3b634085507ab)

Материал с пользой к коммиту:

* [Docker](https://docs.docker.com/engine/reference/builder/)
* [docker-compose](https://docs.docker.com/compose/)
* [Django startproject](https://docs.djangoproject.com/en/3.2/ref/django-admin/#startproject)
* [docker-compose run](https://docs.docker.com/compose/reference/run/)

# Commit #3

Тут на самом деле целая пачка коммитов некоторые с ошибками xD, прошу вас так не делать! =).

Давайте попробуем прикоснуться к прекрасной штуке как **_CI_**, для этого сделайте авторизацию через ваш `github`
аккаунт в
https://travis-ci.com/, как все успешно выполните `Travis-CI` должен будет увидеть ваш репозиторий в `github`.

Прежде чем начинать стоит понять [что такое CI](https://www.atlassian.com/continuous-delivery/continuous-integration)
и для чего нужен [code linting in Python](https://realpython.com/python-code-quality/)

Давайте попробуем запустить наш `Pipeline` с помощью `Travis-CI`. Для этого нужно задать конфигурационный файл и правила
для Flake8
[в этом коммите](https://github.com/temirlan100/recipe-app-api/commit/7d0f59e8bf96b2a8f36931c3373d978a9ca29904). Это
описание для `Travis-CI` что нужно делать, а именно стоит обратить внимание на эту команду
`docker-compose run app sh -c "python manage.py test && flake8"`, то есть начинается прогон тестов (которых у нас пока
нет) и проверка стиля кода нашего приложения. При успешном сценарии на сайте https://travis-ci.com/ во вкладке
build-history будет ваша первая успешная сборка. После каждого вашего `push` в
`github`, `Travis-CI` будет сам запускать билд.

Имеет смысл сделать маленькие
оптимизации [тут](https://github.com/temirlan100/recipe-app-api/commit/81a82330d92a105aeb3cb6a71ffbe3035d16336d)
и [здесь](https://github.com/temirlan100/recipe-app-api/commit/6b16e98178b48d7c7ed892ebacc6d3af4fde7cef)
попробуйте разобрать для чего они нужны ; )

Материал с пользой к коммиту:

* [About Flake8](https://flake8.pycqa.org/en/latest/)
* [Work with Travis-CI](https://docs.travis-ci.com/user/tutorial/)

# Commit #4

Перейдем же к TDD, если коротко то представьте что вы сперва пишите тест к функции которой еще нет и только потом саму
функцию,
[но более подробно можно тут глянуть](https://habr.com/ru/company/ruvds/blog/450316/), но`` и TDD не панацея =) но мы
изучаем ведь это интресно.

В данном коммите очень простые функции которые не относятся к проекту в целом, чтобы понять на кончиках пальца о чем
речь. После того как напишите тесты и функции к ним попробуйте запустить
команду `docker-compose run app sh -c "python manage.py test && flake8"`
ваши 2 теста должны быть успешно пройдены и вывести такой текст
**_Ran 2 tests in 0.69s_**.

[Простые тесты Click!](https://github.com/temirlan100/recipe-app-api/commit/630874e713c0324bf4f0734fbef7a7c239af847e)

Материал с пользой к коммиту:

* [django admin tests](https://docs.djangoproject.com/en/3.2/ref/django-admin/#test)
* [unit tests core python](https://docs.python.org/3/library/unittest.html#assert-methods)
* [unit tests with django](https://docs.djangoproject.com/en/3.2/internals/contributing/writing-code/unit-tests/)

# Commit #5

Прежде чем приступить можно удалить файлы `calc.py`, `tests.py`.

Теперь будем кастомизировать Django user model. Давайте создадим приложение core с помощью Django для этого в терминал
нужно ввести
`docker-compose run app sh -c "python manage.py startapp core"` на уровне папки `app` и файла `.flake8` у вас появится
папка `core`. Стоит сразу удалить файлы `tests.py` так как не надо писать все тесты в одном файле не по **_Clean code_**
это, в замен создайте py директорию (c __init__.py файлом) tests. Далее можно удалить view.py так как будет `REST`
сервис. После всего нужно добавить core приложение в настройки Django в список `INSTALLED_APPS`.

В модели описываются поля, модель это представление таблицы в БД, а поля модели это колонки. После того как вы создали
модель, необходимо добавить это в настройки Django
`AUTH_USER_MODEL = 'core.User'`, далее нужно сделать миграцию для этого введите следующую
команду `docker-compose run app sh -c "python manage.py makemigrations core"`
и у вас появится папка `migrations` c первым файлом миграции.

Далее можете списывать тест запускать как ранее, видеть как он падает и писать к нему функционал. В итоге у вас должно
быть
**_Ran 4 tests in 0.58s_**.

[Customize django User Model Click!](https://github.com/temirlan100/recipe-app-api/commit/d830a3f770f814b620055d64352941ac0042a45a)

Материал с пользой к коммиту:

* [django startapp](https://docs.djangoproject.com/en/3.2/ref/django-admin/#startapp)
* [apps](https://docs.djangoproject.com/en/3.2/ref/settings/#installed-apps)
* [User model](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model)
* [get user model](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#django.contrib.auth.get_user_model)
* [check password](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser.check_password)
* [abstract base user](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser)
* [Base user manager](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#django.contrib.auth.models.BaseUserManager)
* [permission mixin](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#django.contrib.auth.models.PermissionsMixin)
* [super user](https://docs.djangoproject.com/en/3.2/ref/django-admin/#createsuperuser)
* [custom user model](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model)

# Commit #6

Теперь давайте поработаем над функционалом в административной панели которая представляет штанга по умолчанию. Панель
находится по адресу localhost:port/admin, но сейчас у вас будет ошибка, как ее исправить будет в следующих коммитах.

Помните мы про TDD подход. Давайте сделаем тесты для таких вещей как:

* Просмотр списка пользователей
* Просмотр конкретного пользователя
* Доступность страницы редактирования пол-ля
* Доступность страницы создания пол-ля

Подожди! Подумаете вы. Кого мы вообще будем смотреть?! Для этого есть метод `setUp` советую внимательно изучить его. И
далее станет ясно как работают тесты
`test_user_listed`, `test_user_change_page`.

Саму реализацию делаем через **_Django-admin_**, в основном тут только объявление полей все остальное есть из коробки,
да штанга тут очень крута!

[Funcs for users in Django-admin Click!](https://github.com/temirlan100/recipe-app-api/commit/e34c813aba6a5f145f5c0cf6da30957b944f9629)

Материал с пользой к коммиту:

* [django-admin](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/)
* [django fieldsets](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets)

# Commit #7

Все время мы работали с базой и по умолчанию штанга использует базу
[SQLite](https://www.sqlite.org/index.html) это не плохая файловая БД и обычно ее используют для production целей в
мобильных клиентах, но для бэка мы возьмем базу [PostgreSQL](https://www.postgresql.org/).

Теперь давайте добавим контейнер с БД в наш композ файл
(ради всего не поднимайте production базу в контейнере делайте это на отдельной виртуальной машине или сервере!). Так же
вы увидите в композ файле в `db` тэг `environment` так же не делайте так в production среде это чувствительные данные и
их надо хранить в хранилище секретов.

Для того чтобы наше django-приложение работало с базой нужен драйвер для этого есть библиотека `psycopg2`. И не забудьте
сделать настройки в `DATABASES` переменной.

Теперь сделаем промежуточную проверку. Для этого стяните
[данный коммит](https://github.com/temirlan100/recipe-app-api/commit/739ea4c628422a2cd638bce8f8baa9e6118a4918). Напишите
команду `docker-compose build` чтобы убедится что все собирается без ошибок. Но если вы попробуете набрать
`docker-compose run app sh -c "python manage.py runserver 0.0.0.0:8000"`
у вас все сломается + ко всему билд в Travis-CI упадет, но на данном этапе так и должно быть! xD

А как тестить базу?! Для этого есть понятие как [mocking](https://en.wikipedia.org/wiki/Mock_object). Так вот для
мокания объектов внимательно посмотрите на файлы
`test_commands.py` и `wait_for_db`. Чтобы у вас теперь все корректно запускалось, очистите контейнеры с помощью
комманды `docker-compose down -v`. Далее попробуйте поднять приложение которое общается с базой через
`docker-compose up` тут в логах вы увидите успешный запуск приложения и базы в двух разных контейнерах выйти из режима
можно через `ctrl+c`. И после всего вы можете успешно прогнать тесты
`docker-compose run app sh -c "python manage.py test && flake8"`.

И теперь можно зайти в админку `localhost:8000/admin`, кстати чтобы не видеть логи в режиме онлайн можно запустить
контейнеры в режиме демона `docker-comnpose up -d`, а сами логи контейнеров можно посмотреть
так `docker logs container_id -f --tail 50`. Чтобы создать админа воспользуйтесь
командой `docker-compose run app sh -c "python manage.py createsuperuser"`
далее задаете почту и пароль, если после создания у вас не происходит вход в админку штанги то
сделайте [этот фикс](https://github.com/temirlan100/recipe-app-api/commit/77730211cc105a2d215f398dd77e100c5c03fd5a).

[App with DB Click!](https://github.com/temirlan100/recipe-app-api/commit/42e6cd4dab99f9c4a5875a07bde323903e156fe7)

Материал с пользой к коммиту:

* [envs](https://docs.docker.com/compose/environment-variables/)
* [image of postgre](https://hub.docker.com/_/postgres/)
* [depends_on](https://docs.docker.com/compose/compose-file/#depends_on)
* [psycopg2](https://pypi.org/project/psycopg2/)
* [settings DATABASE](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-DATABASES)
* [os environ](https://docs.python.org/3/library/os.html#os.environ)
* [django-admin commands](https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/#module-django.core.management)
* [call_command](https://docs.djangoproject.com/en/3.2/ref/django-admin/#django.core.management.call_command)
* [djamgo unit test wait for DB](https://stackoverflow.com/questions/52621819/django-unit-test-wait-for-database)

# Commit #8

Сделаем модуль по управлению пользователями. Сперва необходимо создать
приложение `docker-compose run --rm app sh -c "python manage.py startapp user"`. Из модуля можно удалить `migrations`
, `admin`, `test`, создать python директорию `tests`(папка с __init__ файлом внутри). Теперь добавим наш модуль в
настройки `INSTALLED_APPS`. В настройки еще нужно добавить два приложения это `rest_framework`
для простого создания **_ENDPOINT_** по _**REST**_ к приложению и
`rest_framework.authtoken` для работы с ключами чтобы наши
**_ENDPOINT_** были доступны тому кому
нужно. [Необходимый коммит](https://github.com/temirlan100/recipe-app-api/commit/9e80b9778ad100f505fa1207b88b73f814a97735)
.

А теперь сделаем тест для создания пользователя, давайте сделаем разбивку нужно сделать тесты на создания, проверка что
существует и длинна пароля должна быть не менее 5 символов. Если вы запустите
тесты `docker-compose run --rm app sh -c "python manage.py test && flake8"`
тогда тесты не пройдут, так как функционала еще нет.
[Коммит на тесты](https://github.com/temirlan100/recipe-app-api/commit/9e95177528285326eae1bc0fb5e7ee736439145d)
и [коммит на покрытие тестов](https://github.com/temirlan100/recipe-app-api/commits/main).

Напишем тесты и функционал для работы с [токенами](https://en.wikipedia.org/wiki/Security_token). Мы сделаем успешный
тест где токен выдается и несколько не успешных
сценариев [вот коммит](https://github.com/temirlan100/recipe-app-api/commit/379c86dfb5f245712dde492f9a6fb469c03d7b32).

Сделайте проверку через браузер, перейдите по ссылке
`http://localhost:8000/api/user/create/` и создайте пользователя, затем перейдите `api/user/token/` зайдите под
пользователеи и получите в ответ сгенерированный ключ-токен.

Поработаем с функционалам и тестами для самого пользователя, а именно, авторизация, просмотр профиля и редактирование.
Это уже не открытые
_**API**_ и лучше их вынести в отдельный класс `PrivateUserApiTests` и уже с ним детально
работать, [тесты и функционал](https://github.com/temirlan100/recipe-app-api/commit/d55170346804d2af795cd4407a19388aaef16673)
.

Проверка браузера, перейдя по ссылке `api/user/me/`, НО только после того как получили токен и вставьте его через
расширение в хроме,
`Authorization`: `Token your_token_here` и вы получите данные по авторизованному пользователю. Там же доступны
методы `PUT` и `PATCH`.

Материал с пользой к коммиту:

* [model serializer](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer)
* [create api view](https://www.django-rest-framework.org/api-guide/generic-views/#createapiview)
* [token](https://www.django-rest-framework.org/api-guide/authentication/#by-exposing-an-api-endpoint)
* [Mod header](https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj)
* [retrieve update api view DRF](https://www.django-rest-framework.org/api-guide/generic-views/#retrieveupdateapiview)

# Commit #9

Нужно сделать тэги, чтобы потом было удобно сортировать, фильтровать данные по приложению, для этого предлагаю вынести в
отдельное django приложение `docker-compose run --rm app sh -c "python manage.py startapp recipe"`
и можно удалить оттуда `models`, `admin`, `migrations`,`tests`
также изменить и добавить приложение в настройки `INSTALLED_APPS`,
[коммит для проверки.](https://github.com/temirlan100/recipe-app-api/commit/837e819651e7c9ddeded74e0769ca421c3bf7e34)

Необходимо по _**FK**_ связать таблицу тэгов с пользователями, для этого создается модель и не забываем про миграции при
каждой новой модели `docker-compose run --rm app sh -c "python manage.py makemigrations"`.

Разделим данные API на public & private, приватные апи доступны тем кто авторизован, иначе 401. Для авторизованных
пользователей можно протестировать доступные теги для пользователя и лимиты по выдаче на будущей странице.

[Tags API and tests Click!](https://github.com/temirlan100/recipe-app-api/commit/395adad2ac42d7cde0f134973d3bab7f120b1cdd)

Материал с пользой к коммиту:

* [model.str](https://docs.djangoproject.com/en/3.2/ref/models/instances/#django.db.models.Model.__str__)
* [model admin](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin)
* [foreign key](https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.ForeignKey)
* [FK delete](https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.ForeignKey.on_delete)
* [HTTP codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)
* [Model serializer](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer)
* [Model view set](https://www.django-rest-framework.org/api-guide/viewsets/#genericviewset)
* [Custom view set](https://www.django-rest-framework.org/api-guide/viewsets/#example_3)

# Commit #10

Запилим ингредиенты(кулинарные =)) в нашем приложении! После создания модели, сделайте миграцию, чтобы в БД была нужная
табличка.

[Ingredients Click!](https://github.com/temirlan100/recipe-app-api/commit/050f608182d07538a0b694a3ec86e3f7d78e7f6f)

# Commit #11

Какое же приложение с рецептами без самих рецептов! Настало время их написать. Понятное дело что нужно добавить модель
для рецептов и конечно же сделать миграцию `docker-compose run --rm app sh -c "python manage.py makemigrations core"`.

[Recipe Click!](https://github.com/temirlan100/recipe-app-api/commit/1c7e44f2f1c4c1a046fbf4f32bb4b197ea233444)

Материал с пользой к коммиту:

* [many-to-many](https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.ManyToManyField)
* [PK DRF](https://www.django-rest-framework.org/api-guide/relations/#primarykeyrelatedfield)
* [Get serialize class](https://www.django-rest-framework.org/api-guide/generic-views/#get_serializer_classself)
* [getattr](https://docs.python.org/3/library/functions.html#getattr)
* [Snippets with user](https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/#associating-snippets-with-users)

# Commit #12

Сейчас вы сможете увидеть как заливаются различные файлы. Но сперва необходимо сделать настройки для работы с файлами.
Внимательно
просмотрите [данный коммит](https://github.com/temirlan100/recipe-app-api/commit/6c4f086c869c35c8d62865c510b6a483bff7a555), 
в нем содержатся нужные параметры, после изменений сделайте `build`
образа через `docker-compose build` и для уверенности еще раз прогоните
тесты `docker-compose run --rm app sh -c "python manage.py test && flake8"`. В модель рецептов добавилось новое поле для
картинки, перед тестами нужно сделать
миграции `docker-compose run --rm app sh -c "python manage.py makemigrations core"`.

[Upload file Click!](https://github.com/temirlan100/recipe-app-api/commit/775b2acaabae087080d028b35933bd9cf66ba8f9)

Материал с пользой к коммиту:

* [image field](https://docs.djangoproject.com/en/3.2/ref/models/fields/#imagefield)
* [Pillow](https://pillow.readthedocs.io/en/stable/)
* [UUID](https://docs.python.org/3/library/uuid.html#uuid.uuid4)
* [File upload](https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.FileField.upload_to)
* [named temporary file](https://docs.python.org/3/library/tempfile.html#tempfile.NamedTemporaryFile)
* [extra route DRF](https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing)

# Commit #13

И завершающий этап, это возможность фильтрации наших сущностей.

[Filters Click!](https://github.com/temirlan100/recipe-app-api/commit/da4b75a4212fe57be24d3b3ff3381e118d275d8b)

###### Заключение
Спасибо что, дошли до этого места! Вы почерпнули для себя много полезных и важных концепций которые можно применять
у себя. В итоге вы лучше стали понимать:
* **REST API**;
* **Конфигурация проекта с помощью Docker**;
* **Конфигурация Travis-CI**;
* **Создания API(endpoints)**;
* **Загрузка картинок**;
* **И конечно же Unit тесты**;

Если __Вам__ интересно двигаться дальше и понять как это приложение катить в __AWS!__, [тогда советую вам этот курс! =))](https://github.com/temirlan100/recipe-app-api) 

















