#  RUN ::
#  uvicorn main:app --reload
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import router, gpt
# from routers import test

app = FastAPI()

# 라우터 등록
# app.include_router(test.router)
app.include_router(router.router)
app.include_router(gpt.router)

# CORS 설정
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5173/",
    "https://hackathon-team1-frontend.vercel.app"
    # 프론트엔드 배포 주소
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, # allow cookie  (JWT)
    allow_methods=["*"],
    allow_headers=["*"],
)

# root
@app.get("/", summary="root")
async def root():
    result = {'message': "일석일조 화이팅!!"}
    return result