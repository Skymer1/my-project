FROM python:3.10

RUN pip install flask

WORKDIR /flaskapp
ADD app.py . 

ENV FLASK_ENV=development

CMD python3 app.py
