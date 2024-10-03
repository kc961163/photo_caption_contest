# app/main.py

from fastapi import FastAPI

from .routers import auth, captions, images, users

app = FastAPI()

# Include authentication router
app.include_router(auth.router)

# Include other routers
app.include_router(users.router)
app.include_router(captions.router)
app.include_router(images.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
