import uvicorn
from app.main import app

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        #host="0.0.0.0",
        host="localhost",
        port=8080,
        reload=True,
        log_level="info"
    ) 