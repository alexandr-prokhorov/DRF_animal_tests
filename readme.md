Платформа тестирования

Платформа тестирования включает в себя разделы:

- Пользователи
- Секции с типом транспорта

Виртуальное окружение используемое для проекта: venv

1) После настройки виртуального окружения установите зависимости из файла requirements.txt

```bash
  pip install -r requirements.txt
```

2) Заполните файл .env согласно файла .env_sample

3) Работа с базой данных MSSQL

Выполните следующие действия:

3.1. создайте Базу данных при помощи команды

```bash
  python manage.py ccdb
```

3.2. Создайте миграции при помощи команды

```bash
  python manage.py makemigrations
```

3.3. Примените созданные миграции при помощи команды

```bash
  python manage.py migrate
```

3.4. Выполните команду для создания пользователей

```bash
  python manage.py ccsu
```

3.5. Выполните команду для заполнения базы данных используя фикстуры

```bash
   python manage.py loaddata sections.json
```

3.6. Выполните команду для запуска приложения

```bash
  python manage.py runserver
```

4) Работа с Docker

Для работы с Docker выполните следующие действия:

```bash
  docker-compose up -d --build
```

Модели используемые в проекте:

Sections:

- title - название типа транспорта
- Description - описание типа транспорта

Section Contents:

- Section - выбор к какому виду транспорта, относится ТС
- Title - название ТС
- Content - описание ТС

Questions:

- Section - выбор к какому виду транспорта, относится вопрос по ТС
- Description - описание действия для ответа
- Question - вопрос
- Answer - ответ

User с полями:

- username - никнейм пользователя
- email - электронная почта пользователя
- role - роль пользователя (ADMIN or MODERATOR or USER)
- first_name - имя пользователя (может быть пустым)
- last_name - фамилия пользователя (может быть пустым)
- phone - телефон пользователя (может быть пустым)
- is_active - признак активности пользователя по умолчанию True

Пагинация

- Реализована пагинация ...

Разрешения (Permissions)

- Реализованы кастомные разрешения для пользователя с ролью USER, MODERATOR, ADMIN

Views модели Sections (тип транспорта)

- SectionListAPIView (показывает список всех типов транспорта)
- SectionCreateAPIView (добавление нового типа транспорта)
- SectionRetrieveAPIView (получение информации о типе транспорта)
- SectionUpdateAPIView (изменение типа транспорта)
- SectionDestroyAPIView (удаление типа транспорта)
- ContentListAPIView (показывает весь список ТС)
- ContentCreateAPIView (добавление ТС)
- ContentRetrieveAPIView (получение информации о ТС)
- ContentUpdateAPIView (изменение информации о ТС)
- ContentDestroyAPIView (удаление ТС)
- QuestionListAPIView (просмотр всех вопросов теста)
- QuestionRetrieveAPIView (получение вопроса для ответа на него)

Views модели Users (пользователи)

- UserListAPIView (показывает список всех пользователей)
- UserCreateAPIView (добавление нового пользователя)
- UserRetrieveAPIView (получение информации о пользователе)
- UserUpdateAPIView (изменение информации о пользователе)
- UserDestroyAPIView (удаление пользователя)
- UserTokenObtainPairView (получение токена для пользователя)