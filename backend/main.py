import uvicorn

def main()-> None:
    """starts the fastapi application using uvicorn"""
    uvicorn.run("backend.app:app",host="0.0.0.0",port=8000,reload=True)

if __name__=="__main__":
    main()


