import sys, os
import uvicorn

# sys.path 설정을 맨 위로 이동
base_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(base_dir + "/back")  # back 폴더를 추가

from app.main import app  # 이제 app.main을 찾을 수 있음

if __name__ == "__main__":
    uvicorn.run(
        app,  # 직접 app 객체 전달
        host="localhost",
        port=8000,
        reload=True,
        log_level="info"
    )