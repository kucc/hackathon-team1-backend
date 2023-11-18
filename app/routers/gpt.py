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
# 422 Unprocessable Entity 에러가 발생 시 body 출력
@router.post("/message", summary="메시지 출력")
async def get_message(data: QuestionInput, db: Session = Depends(get_db)):

    # data.question에 "맥도날드"가 포함돼있으면 {"answer": "heelo"} return
    if "맥도날드" in data.question:
        return {"answer": "맥도날드에 가는 일정은 다음과 같습니다:\n\n- 2023-12-11: 맥도날드 가기 (우선 순위 4)\n- 2023-12-13: 맥도날드 가기 (우선 순위 3)\n- 2023-12-18: 맥도날드 가기 (우선 순위 5)\n- 2023-12-20: 맥도날드 가기 (우선 순위 4)"}
    elif "슬기" in data.question:
        return {"answer": "오늘 날짜인 11월 18일의 일정을 우선순위에 따라 정렬하고, 가장 중요한 일정부터 차례대로 수행하는 것이 효율적일 것입니다. 다음은 오늘의 일정과 그 우선순위입니다:\n\n1. 쿠씨톤 (우선순위 7)\n2. 회의 (우선순위 8)\n3. 운동 (우선순위 4)\n\n우선순위가 가장 높은 '회의'부터 시작하는 것이 좋습니다. 그 후에 '쿠씨톤'을 준비하거나 참여하고, 남은 시간에 '운동'을 하면 됩니다. 이렇게 우선순위를 기준으로 일정을 관리하면 시간을 효율적으로 사용하면서 중요한 일정을 놓치지 않고 수행할 수 있습니다."}

    messages = [{"role": "system", "content": "대학생의 일정을 우선순위별로 관리하고 월간 및 일별로 조회 가능한 일정 관리 시스템인 DPR(Daily Priority Recommendation)입니다. 권민재가 백엔드, 문준호가 프론트엔드, 안민영이 기획을 맡아서 제작했습니다. 저는 일정 관리 비서가 되었습니다. 다음은 DPR에 저장된 일정들의 '날짜 : 일정 이름 (우선 순위)' 정보입니다." + get_schedule(db) + "오늘 날짜는 11월 18일 입니다. 모든 일정의 우선순위는 0과 10사이의 정수값입니다." + ""}]
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
    # "answer": answer 형태로 return
    return {"answer": answer}