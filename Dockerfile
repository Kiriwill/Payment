FROM python:3.7.2

LABEL Author="Willian Pacheco"
LABEL Version="0.1"

RUN mkdir /Api_sqlAl

WORKDIR /Api_sqlAl

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8081

CMD ["python", "app.py"]
