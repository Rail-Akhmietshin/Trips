This project is designed to help people travel between Russian cities without service fees, paying only for the trip itself directly to the driver.

!!! After cloning the repository, enter personal parameters in the .env.prod and .env.prod.db files !!!

!!! It is necessary to grant write permissions for the root and its incoming files and folders (* chmod -R 755 (your path to the root folder)  ) !!!

Starting the project build:

* docker-compose up -d --build

After successfully running the project in Docker, write the following commands in the console to perform migrations and collect static files:

* docker-compose exec web python manage.py migrate --noinput
* docker-compose exec web python manage.py collectstatic --no-input --clear

The application will be available at: http://localhost:1337
