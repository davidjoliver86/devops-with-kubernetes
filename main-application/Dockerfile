FROM python:3.9-alpine
WORKDIR /app

# requirements
COPY requirements.txt /app
RUN pip install -r requirements.txt

# deploy app
COPY main /app/main
COPY .flaskenv /app

# run
EXPOSE 5000
CMD ["flask", "run"]
