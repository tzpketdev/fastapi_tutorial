from fastapi import FastAPI, Path
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse
app = FastAPI()

#create FastApi object
@app.get("/")
#use method get
#
async def root():
    return {"message": "Hello World"}

@app.get("/add")

async def add(x:int, y: int) -> int:
    return x+y
#
@app.get("/double/{number}")

async def double(number:int) -> int:
    return number*2

# @app.get("/welcome/{name})
#
#
# async def welcome(name: str = Path(min_length=2, max_length=20)) -> str:
#     return f"Good luck, {name}!"


@app.get("/text")
async def get_text():
    content = "In da block"
    return PlainTextResponse(content=content)

@app.get("/html")
async def get_text():
    content = "<h1>Bab</h1>"
    return HTMLResponse(content=content)

@app.get("/file")
async def get_text():
    content = "index.html"
    content = "index.html"
    return FileResponse(content,
                        media_type="application/octet-stream",
                        filename= "index2.html")
# @app.get("/phone/{number}")
# def phone_number(number: str = Path(regex=)):
#     return {"phone": number}
#

