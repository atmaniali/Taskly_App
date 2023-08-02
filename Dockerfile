FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR home/user/src/app
COPY . /home/user/src/app

RUN pip install -r requirements.txt

#CMD ["python", "manage.py", "runserver"]
#ENTRYPOINT ["sh","entrypoint.sh"]