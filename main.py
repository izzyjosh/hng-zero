from fastapi import FastAPI
from utils import me, detailed_response
import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()


app = FastAPI()

@app.get("/me")
async def get_profile():
    response = await detailed_response(me)
    return response


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run( "main:app", host="0.0.0.0", port=port, reload=True)
