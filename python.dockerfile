FROM python:3.12-alpine

WORKDIR /data/ToDo

RUN pip install fastapi \
    && pip install uvicorn \
    && pip install psycopg2-binary

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]