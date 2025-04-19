from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import EmployeeKPITracker
from ..schemas import EmployeeKPIOut

router = APIRouter()

@router.get("/api/kpis", response_model=list[EmployeeKPIOut])
def get_kpis(db: Session = Depends(SessionLocal)):
    return db.query(EmployeeKPITracker).all()