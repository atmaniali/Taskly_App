# bin/sh
echo "RUN ENTRYPOINT"
python manage.py makemigrations
python manage.py migrate
exec "@"