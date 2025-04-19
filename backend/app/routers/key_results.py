from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import KeyResult
from ..schemas import KeyResultOut

router = APIRouter()

@router.get("/api/key-results", response_model=list[KeyResultOut])
def get_key_results(objective_id: str, db: Session = Depends(SessionLocal)):
    return db.query(KeyResult).filter(KeyResult.objective_id == objective_id).all()
