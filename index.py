from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app = FastAPI()

class SearchRequest(BaseModel):
    file_path: str
    query: str


# Allow CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/files')
def files():
    from utils.get_files import list_files
    result = list_files()
    return result


@app.get("/execute")
def execute_query(option: str, user_input: str):
    from models.azmath_core import execute_query
    result = execute_query(option,user_input)
    return result


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    from utils.upload import upload_file
    result = upload_file(file)
    return result


@app.post("/search")
async def search(request: SearchRequest):
    from models.azmath_files_search import search_files
    file_path = request.file_path
    query = request.query
    result = search_files(file_path,query)
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

