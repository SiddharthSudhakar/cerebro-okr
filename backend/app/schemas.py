from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import date

class OrganizationalGoalOut(BaseModel):
    objective_id: UUID
    objective_name: str
    class Config:
        orm_mode = True

class KeyResultOut(BaseModel):
    key_result_id: UUID
    key_result_name: str
    target_figure: float
    class Config:
        orm_mode = True

class EmployeeOut(BaseModel):
    employee_id: UUID
    employee_name: str
    group_id: Optional[UUID]
    department_id: Optional[UUID] 
    role_id: Optional[UUID]
    level_id: Optional[UUID]
    reporting_manager_id: Optional[UUID]
    class Config:
        orm_mode = True

class ProjectAllocationOut(BaseModel):
    employee_id: UUID
    primary_project_id: Optional[UUID]
    second_project_id: Optional[UUID]
    third_project_id: Optional[UUID]
    fourth_project_id: Optional[UUID]
    fifth_project_id: Optional[UUID]
    sixth_project_id: Optional[UUID]
    seventh_project_id: Optional[UUID]
    eighth_project_id: Optional[UUID]
    ninth_project_id: Optional[UUID]
    tenth_project_id: Optional[UUID]
    eleventh_project_id: Optional[UUID]
    twelfth_project_id: Optional[UUID]
    thirteenth_project_id: Optional[UUID]
    fourteenth_project_id: Optional[UUID]
    fifteenth_project_id: Optional[UUID]
    class Config:
        orm_mode = True

class EmployeeKPIOut(BaseModel):
    tracker_id: UUID
    employee_id: UUID
    key_result_id: UUID
    metric_id: Optional[UUID]
    actual_value: Optional[float]
    status: Optional[str]
    last_updated: Optional[date]
    comments: Optional[str]

    class Config:
        orm_mode = True

class MetricUnitOut(BaseModel):
    metric_id: UUID
    metric_name: str
    class Config:
        orm_mode = True

class GroupOut(BaseModel):
    group_id: UUID
    group_name: str
    class Config:
        orm_mode = True

class DepartmentOut(BaseModel):
    department_id: UUID
    department_name: str
    class Config:
        orm_mode = True

class ProjectOut(BaseModel):
    project_id: UUID
    project_name: str
    class Config:
        orm_mode = True

class LevelOut(BaseModel):
    level_id: UUID
    level_name: str
    class Config:
        orm_mode = True

class RoleOut(BaseModel):
    role_id: UUID
    role_name: str
    class Config:
        orm_mode = True

