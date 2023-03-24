FROM python:3.9

WORKDIR /app

COPY . /app

ADD app.py .

RUN pip install -r requirements.txt

EXPOSE 3000

CMD python ./app.py