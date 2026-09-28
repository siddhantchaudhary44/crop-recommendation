from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.api.api import api_router

app=FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8501",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def middleware(request: Request, call_next):
    response = await call_next(request)
    return response

app.include_router(api_router)