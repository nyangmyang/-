import uvicorn
import os, sys

file_path = os.path.abspath("app/main.py")
uvicorn.run(file_path + ":app", ...)

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        #host="0.0.0.0",
        host="localhost",
        port=8080,
        reload=True,
        log_level="info"
    ) 
