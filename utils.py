from datetime import datetime, timezone
import http
import httpx
from fastapi import HTTPException, status


# Setup for user data
class User:
    def __init__(self, email, name, stack) -> None:
        self.name = name
        self.email = email
        self.stack = stack

    def to_dict(self) -> dict:
        return {
                "email": self.email,
                "name": self.name,
                "stack": self.stack
                }

me = User("calebayuba222@gmail.com", "Joshua Joseph", "Python/FastAPI")


# Function to fetch from catfact url
async def fetch_cat_data(url):

    async with httpx.AsyncClient(timeout=20) as client:
        try:
            response = await client.get(url)
            response.raise_for_status()

            return (response.json(), "success")

        except httpx.TimeoutException:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Request timed out")

        except httpx.ConnectError:
            raise HTTPException(status_code=503, detail="No internet connection, unable to reach upstream server")

        except Exception as e:
            raise HTTPException(status_code=400, detail=f"{e}")


# Detailed response format
async def detailed_response(user) ->  dict:

    url = "https://catfact.ninja/fact"

    fact, success = await fetch_cat_data(url)

    timestamp = datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")

    return {
            "status": success,
            "user": user.to_dict(),
            "timestamp": timestamp,
            "fact": fact.get("fact")
        }
