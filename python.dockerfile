FROM python:3

WORKDIR /data/ToDo
RUN pip install --upgrade pip \
    && pip intall fastapi \
    && pip install uvicorn \
    && pip install psycopg2-binary

EXPOSE 8000

CMD ["uvvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]