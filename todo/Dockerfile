FROM python:3.9-alpine
COPY todo /app/todo
COPY requirements.txt /app
COPY .flaskenv /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run"]
