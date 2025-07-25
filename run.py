import sys, os
import uvicorn

if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.dirname(__file__))  # 현재 스크립트 위치 절대경로

    sys.path.append(base_dir + "/back/app")  # app 폴더 sys.path 에 추가
    
    uvicorn.run(
        "main:app",
        host="localhost", # 테스트 용으로 로컬 호스트로 변경함 
        port=8000,
        reload=True,
        log_level="info"
    )
