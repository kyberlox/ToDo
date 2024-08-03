import fastapi
from fastapi.middleware import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import psycopg2

conn = psycopg2.connect(dbname='pdb', user='kyberlox', password='4179', host='127.0.0.1', port='5432')
cursor = conn.cursor()

app = FastAPI()

origins = [
    "http://127.0.0.1:8000",
    "http://localhost:8000"
]

app.add_midlware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Accept", "Location", "Allow", "Content-Disposition", "Sec-Fetch-Dest"]
)

app.mount("/public", StaticFiles(directory="public"), name="public")