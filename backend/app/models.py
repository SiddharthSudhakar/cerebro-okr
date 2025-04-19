from sqlalchemy import Column, String, Text, ForeignKey, Numeric, Date
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .database import Base

class OrganizationalGoal(Base):
    __tablename__ = "organizational_goals"
    objective_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    objective_name = Column(String, nullable=False)
    objective_description = Column(Text)

class KeyResult(Base):
    __tablename__ = "organizational_key_results"
    key_result_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    objective_id = Column(UUID(as_uuid=True), ForeignKey("organizational_goals.objective_id"))
    key_result_name = Column(String, nullable=False)
    metric_id = Column(UUID(as_uuid=True))
    target_figure = Column(Numeric)
    metric_units = Column(String)
    metric_figures = Column(Numeric)
    department_id = Column(UUID(as_uuid=True), ForeignKey("master_departments.department_id"))
    group_id = Column(UUID(as_uuid=True), ForeignKey("master_groups.group_id"))
    role_id = Column(UUID(as_uuid=True), ForeignKey("master_roles.role_id"))
    target_id = Column(UUID(as_uuid=True))

class Employee(Base):
    __tablename__ = "employees"
    employee_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    employee_name = Column(String, nullable=False)
    group_id = Column(UUID(as_uuid=True), ForeignKey("master_groups.group_id"))
    department_id = Column(UUID(as_uuid=True), ForeignKey("master_departments.department_id"))
    role_id = Column(UUID(as_uuid=True), ForeignKey("master_roles.role_id"))
    level_id = Column(UUID(as_uuid=True), ForeignKey("master_levels.level_id"))
    reporting_manager_id = Column(UUID(as_uuid=True), ForeignKey("employees.employee_id"))

class ProjectAllocation(Base):
    __tablename__ = "project_allocations"
    employee_id = Column(UUID(as_uuid=True), ForeignKey("employees.employee_id"), primary_key=True)
    primary_project_id = Column(UUID(as_uuid=True), ForeignKey("master_projects.project_id"))
    second_project_id = Column(UUID(as_uuid=True), ForeignKey("master_projects.project_id"))
    third_project_id = Column(UUID(as_uuid=True), ForeignKey("master_projects.project_id"))
    fourth_project_id = Column(UUID(as_uuid=True), ForeignKey("master_projects.project_id"))
    fifth_project_id = Column(UUID(as_uuid=True), ForeignKey("master_projects.project_id"))
    sixth_project_id = Column(UUID(as_uuid=True), ForeignKey("master_projects.project_id"))
    seventh_project_id = Column(UUID(as_uuid=True), ForeignKey("master_projects.project_id"))
    eighth_project_id = Column(UUID(as_uuid=True), ForeignKey("master_projects.project_id"))
    ninth_project_id = Column(UUID(as_uuid=True), ForeignKey("master_projects.project_id"))
    tenth_project_id = Column(UUID(as_uuid=True), ForeignKey("master_projects.project_id"))
    eleventh_project_id = Column(UUID(as_uuid=True), ForeignKey("master_projects.project_id"))
    twelfth_project_id = Column(UUID(as_uuid=True), ForeignKey("master_projects.project_id"))
    thirteenth_project_id = Column(UUID(as_uuid=True), ForeignKey("master_projects.project_id"))
    fourteenth_project_id = Column(UUID(as_uuid=True), ForeignKey("master_projects.project_id"))
    fifteenth_project_id = Column(UUID(as_uuid=True), ForeignKey("master_projects.project_id"))

class EmployeeKPITracker(Base):
    __tablename__ = "employee_kpi_trackers"
    tracker_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    employee_id = Column(UUID(as_uuid=True), ForeignKey("employees.employee_id"))
    key_result_id = Column(UUID(as_uuid=True), ForeignKey("organizational_key_results.key_result_id"))
    metric_id = Column(UUID(as_uuid=True))
    actual_value = Column(Numeric)
    status = Column(String)
    last_updated = Column(Date)
    comments = Column(Text)

class MetricUnit(Base):
    __tablename__ = "master_metric_units"
    metric_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    metric_name = Column(String, nullable=False)

class Group(Base):
    __tablename__ = "master_groups"
    group_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    group_name = Column(String, nullable=False)

class Department(Base):
    __tablename__ = "master_departments"
    department_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    department_name = Column(String, nullable=False)

class Project(Base):
    __tablename__ = "master_projects"
    project_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_name = Column(String, nullable=False)

class Level(Base):
    __tablename__ = "master_levels"
    level_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    level_name = Column(String, nullable=False)

class Role(Base):
    __tablename__ = "master_roles"
    role_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    role_name = Column(String, nullable=False)


