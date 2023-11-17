# 다음 링크를 많이 참고했습니다: https://velog.io/@djm030/%EC%B1%97GPT%EC%99%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EB%A7%8C%EB%93%9C%EB%8A%94-%EB%82%98%EB%A7%8C%EC%9D%98-%EC%97%B0%EC%95%A0-%EC%BD%94%EC%B9%98-with-FastAPI
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, Response, Request, status, HTTPException, Path
from sqlalchemy.orm import Session
import openai
from pydantic import BaseModel

from database import get_db
from models import K_MainEvent, K_Event

router = APIRouter(prefix="/gpt", tags=["gpt"], responses={404: {"description": "Not found"}})

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY
model = "gpt-4-1106-preview"

# 채팅 기록을 저장할 딕셔너리
# db를 만든다면 이 부분은 필요없다.
chat_history = {"User": {}, "AI": {}}

# 종강일과 모든 일정을 가져와서 문자열로 저장
def get_schedule(db: Session):
    # 종강일 가져오기
    end_date = db.query(K_MainEvent).filter(K_MainEvent.event_name == "종강").first().event_date
    # 모든 일정 가져오기
    events = db.query(K_Event).all()
    # 종강일과 모든 일정을 문자열로 저장
    schedule = f"종강일: {end_date} "
    # priority도 같이 출력
    for event in events:
        schedule += f"{event.event_date}: {event.event_name} ({event.priority})\n"
    return schedule

class QuestionInput(BaseModel):
    question: str


# 메시지 출력 API
@router.post("/message", summary="메시지 출력")
async def get_message(data: QuestionInput, db: Session = Depends(get_db)):
    messages = [{"role": "system", "content": "일정 관리 비서가 되었습니다. 다음은 일정들의 '날짜 : 일정 이름 (우선 순위)' 정보입니다." + get_schedule(db) + "오늘 날짜는 11월 18일 입니다. 모든 일정의 우선순위는 1과 10사이의 정수값입니다." + "이 서비스의 이름은 DPR(Daily Priority Recommendation)입니다. "}]
    user_question = f"{data.question}"
		# 채팅을 구분하기 위해 현재 시간을 가져온다.
    messages.append(
        {
            "role": "user",
            "content": f"""
            question : {user_question}
            """,
        },
    )
    
    # GPT-4 호출과 관련된 코드
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.6,
    )
    answer = response["choices"][0]["message"]["content"]

    return answer