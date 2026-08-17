from fastapi import APIRouter, File, UploadFile
import shutil
from fastapi.responses import FileResponse

router = APIRouter(
    prefix="/file",
    tags=["file"]
)

@router.post("/file")
def get_file(file: bytes = File(...)):
    content = file.decode("utf-8")
    lines = content.split("\n")

    return {
        "line": lines
    }
    
@router.post('/uploadfile')
def upload_file(upload_file: UploadFile = File(...)):
    path = f"files/{upload_file.filename}"
    #with this we are going to store our file into local folder
    with open(path, "w+b") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return {
        'filename': path,
        "type": upload_file.content_type
    }
    
@router.get("/download/{name}", response_class=FileResponse)
def download_file(name: str):
    path = f"files/{name}"
    return path