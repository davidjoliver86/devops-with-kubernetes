FROM python:3.9-alpine
COPY todo /app/todo
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP=todo/hello.py
EXPOSE 5000
CMD ["flask", "run"]
