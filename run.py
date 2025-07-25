import sys, os
import uvicorn
import os, sys

file_path = os.path.abspath("app/main.py")
uvicorn.run(file_path + ":app", ...)

if __name__ == "__main__":
    uvicorn.run(
        app,  # 직접 app 객체 전달
        host="localhost",
        port=8000,
        reload=True,
        log_level="info"
    ) 
