from models import Base, OrganizationalGoal, KeyResult
from database import engine, SessionLocal
import uuid

Base.metadata.create_all(bind=engine)

db = SessionLocal()
db.add_all([
    OrganizationalGoal(
        objective_id=uuid.UUID('11111111-1111-1111-1111-111111111111'),
        objective_name='Increase Engineering Delivery Velocity',
        objective_description='Improve engineering output'
    ),
    KeyResult(
        key_result_id=uuid.uuid4(),
        objective_id=uuid.UUID('11111111-1111-1111-1111-111111111111'),
        key_result_name='Complete 95% of sprint tasks on time',
        metric_id=uuid.uuid4(),
        target_figure=95
    )
])
db.commit()
