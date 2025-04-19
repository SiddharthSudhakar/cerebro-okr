from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import ProjectAllocation
from ..schemas import ProjectAllocationOut

router = APIRouter()

@router.get("/api/allocations", response_model=list[ProjectAllocationOut])
def get_allocations(db: Session = Depends(SessionLocal)):
    return db.query(ProjectAllocation).all()
