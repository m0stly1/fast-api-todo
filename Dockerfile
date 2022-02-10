FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt /app

COPY /app .

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000
