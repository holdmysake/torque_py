from fastapi import FastAPI
from controllers.route_controller import router as route_router

app = FastAPI()
app.include_router(route_router)