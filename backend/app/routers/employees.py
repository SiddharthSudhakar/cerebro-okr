from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Employee
from ..schemas import EmployeeOut

router = APIRouter()

@router.get("/api/employees", response_model=list[EmployeeOut])
def get_employees(db: Session = Depends(SessionLocal)):
    return db.query(Employee).all()