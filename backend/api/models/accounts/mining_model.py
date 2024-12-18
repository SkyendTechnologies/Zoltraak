from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from models.db_helper import db_helper


# Mining task model
class MiningTaskModel(db_helper.Base):
    """
    Represents a mining task performed by an account in the system.

    Attributes:
        id (int): Unique identifier for the mining task.
        account_id (int): ID of the associated account performing the task.
        task_name (str): Name of the mining task.
        task_details (str): Detailed description of the task.
        reward (float): Tokens rewarded upon task completion.
        created_at (datetime): Timestamp when the task was created.
        started_at (datetime): Timestamp when the task started.
        completed_at (datetime): Timestamp when the task was completed.
        status (str): Current status of the task (e.g., pending, running, completed).
        account (AccountModel): The account associated with the task.
    """
    __tablename__ = 'mining_tasks'

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    task_name = Column(String(100), nullable=False)
    task_details = Column(String, nullable=False)
    reward = Column(Float, default=0.0, nullable=False, comment="Tokens rewarded for completing the task")
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    status = Column(String, nullable=False)

    account = relationship("AccountModel", back_populates="mining_tasks")
