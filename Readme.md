Тестовое задание(Создание API)

Для запуска проекта нужно:

установить зависимости из файла requirements:
pip install -r requirements.txt

сделать миграции:
python manage.py makemigrations personal_card  
python manage.py makemigrations
python manage.py migrate

Заполнить базу данных произвольными данными
python manage.py seed personal_card --number={n}  (n - количество записей)

Запустить локальный сервер с настройками из файла 
local_settings.py:  python manage.py --settings=university.local_settings
