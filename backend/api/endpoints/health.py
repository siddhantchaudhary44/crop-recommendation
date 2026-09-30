from fastapi import APIRouter
from backend.schemas.health import HealthResponse
from backend.config import model_version

router=APIRouter()

@router.get("/health")
async def health_check():
    """return health status and model version of the api"""
    return{
    'status':200,
    'app_name':'crop prediction model',
    'model_version':model_version
    }

