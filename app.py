from fastapi import FastAPI
from utils import me, detailed_response
import uvicorn

app = FastAPI()

@app.get("/me")
async def get_profile():
    response = await detailed_response(me)
    return response


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
