from fastapi import FastAPI, File, UploadFile, Body, Response, Cookie
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import HTTPException

import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="public", html=True))



origins = [
    "http://localhost:8000",
    "http://kyberlox.todo"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],#, "OPTIONS", "DELETE", "PATH", "PUT"],
    allow_headers=["Content-Type", "Accept", "Location", "Allow", "Content-Disposition", "Sec-Fetch-Dest"],
)



@app.get("/")
def root():
    return RedirectResponse("http://kyberlox.todo/index.html")

#создание задач
@app.get("/new_task")
def root():
    return RedirectResponse("http://kyberlox.todo/create_task.html")

@app.post("/upload_img")
def create_file(file : UploadFile):
    content_type = file.content_type
    if content_type not in ["image/jpeg", "image/png", "image/gif"]:
        raise HTTPException(status_code=400, detail="Invalid file type")
    else:
        #добавь нумерацию
        #фиксируй в БД
        
        file_path = f"./public/files/{file.filename}"
        with open(file_path, 'wb') as f:
            f.write(file.file.read())
        return {"message": "File saved successfully"}

    #return {"filename" : file.filename}

#создание приоритетов
@app.get("/new_priority")
def root():
    return RedirectResponse("http://kyberlox.todo/create_priority.html")

#страница процесса

#выгрузка файла



#создание задачи

#создание процесса

#загрузка файла