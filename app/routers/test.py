from fastapi import APIRouter, Depends, Response, Request, status
from sqlalchemy.orm import Session

from database import get_db
from models import K_Test

router = APIRouter(prefix="/test", tags=["test"], responses={404: {"description": "Not found"}})

# test 핸들러
@router.get("")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(K_Test).all()
    return users