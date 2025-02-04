from fastapi import FastAPI
from backend_app.database import engine
from backend_app.models import Base
from backend_app.endpoint import router


Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router)
