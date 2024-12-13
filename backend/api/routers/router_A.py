from routers import Routering
@Routering.get("/")
async def root():
    return {"message": "Hello World"}