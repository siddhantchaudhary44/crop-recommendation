from fastapi import APIRouter
from backend.api.endpoints import health,predict

api_router=APIRouter()

api_router.include_router(health.router,tags=["health"])
api_router.include_router(predict.router,tags=["prediction"])
