from fastapi import FastAPI

fastapi = FastAPI()


@fastapi.get("/")
async def main():
    return {"message": "main"}


@fastapi.get("/test")
async def test():
    return {"message": "test"}
