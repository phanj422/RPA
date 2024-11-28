from fastapi import FastAPI
import qrcode.constants
app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/item")
# def read_item(item_id: int, name: str = None, age: int = 0):
#     return {"item_id": item_id, "name": name, "age": age}

# from fastapi import Form
# @app.post("user")
# async def read_user_form(name: str = Form(...), studentcode: str=Form(...), major: str=Form(...)):
#     return{"msg": f"{major} {name}님 ({studentcode}) 반갑습니다."}

# @app.post("/plus")
# async def plus_form(num1 : int = Form(...), num2 : int = Form(...), num3 : int = Form(...), num4 : int = Form(...)):
#     result = num1 + num2
#     result1 = num3 + num4
#     return{"msg" : f"{num1} + {num2} = {result} | {num3} + {num4} = {result1}"}

from fastapi import Form
from fastapi import File, UploadFile
import shutil
from pathlib import Path

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    save_path = Path("static/uploads") / file.filename
    save_path.parent.mkdir(parents=True, exist_ok=True)
    
    with save_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    return {"filename": file.filename, "location": str(save_path)}

from fastapi import File, UploadFile
import shutil
from pathlib import Path
from fastapi.responses import FileResponse

@app.get("/files/{filename}")
async def get_file(filename: str):
    file_path = Path("static/uploads") / filename
    if file_path.is_file():
        return FileResponse(path=file_path, filename=filename)
    else:
        raise HTTPException(status_code=404, detail="File not found")
    
from fastapi.responses import StreamingResponse
import qrcode
from io import BytesIO

@app.post("/qrcode/")
async def generate_qr(data: str = Form(...)):
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format = 'PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    return StreamingResponse(BytesIO(img_byte_arr), media_type="image/png")

from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__=='__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level="info")
    
