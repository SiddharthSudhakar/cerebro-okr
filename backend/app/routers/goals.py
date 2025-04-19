from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import OrganizationalGoal
from ..schemas import OrganizationalGoalOut

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/api/goals", response_model=list[OrganizationalGoalOut])
def get_goals(db: Session = Depends(get_db)):
    return db.query(OrganizationalGoal).all()
