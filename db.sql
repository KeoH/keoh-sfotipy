CREATE DATABASE `django_sfotipy_db`
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;

GRANT ALL PRIVILEGES ON django_sfotipy_db.* TO 'django_user'@'localhost' IDENTIFIED BY 'django-password_001'

WITH GRANT OPTION;
FLUSH PRIVILEGES;