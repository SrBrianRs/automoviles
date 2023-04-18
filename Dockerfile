FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /automoviles
WORKDIR /automoviles
COPY requirements.txt /automoviles/
RUN pip install -r requirements.txt
COPY . /automoviles/
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8080