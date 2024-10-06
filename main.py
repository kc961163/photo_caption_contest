# main.py

from fastapi import FastAPI

from api.auth.controllers import router as auth_router
from api.database.database import Base, engine

# from api.captions.controllers import router as captions_router
# from api.images.controllers import router as images_router
from api.users.controllers import router as users_router

# Uncomment the following line if not using Alembic for migrations
# Base.metadata.create_all(bind=engine)

api = FastAPI(
    title="Photo Caption Contest API",
    description="API for managing photo caption contests.",
    version="1.0.0",
)

# Include routers with prefixes and tags
api.include_router(auth_router, prefix="/auth", tags=["Authentication"])
api.include_router(users_router, prefix="/users", tags=["Users"])
# api.include_router(captions_router, prefix="/captions", tags=["Captions"])
# api.include_router(images_router, prefix="/images", tags=["Images"])


@api.get("/")
def read_root():
    return {"Hello": "World"}
