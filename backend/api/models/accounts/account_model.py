from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from models.db_helper import db_helper

# Account model
class AccountModel(db_helper.Base):
    """
    Represents a user account in the system.

    Attributes:
        id (int): Unique identifier for the account.
        username (str): Username of the account.
        email (str): Email address of the user.
        hashed_password (str): Hashed password for secure authentication.
        created_at (datetime): Timestamp when the account was created.
        updated_at (datetime): Timestamp for the last update to the account.
        is_active (bool): Indicates whether the account is active.
        mining_tasks (list[MiningTaskModel]): Related mining tasks associated with the account.
        wallets (list[WalletModel]): Wallets linked to the account.
    """
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)  # Primary key and indexed for faster lookups
    username = Column(String(50), nullable=False, unique=True)  # Unique username, max length 50
    email = Column(String, nullable=False, unique=True)  # Unique email address
    hashed_password = Column(String, nullable=False)  # Securely hashed password
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)  # Creation timestamp
    updated_at = Column(DateTime, onupdate=datetime.utcnow)  # Timestamp for the last update
    is_active = Column(Boolean, default=True, nullable=False)  # Active status indicator

    # Relationships
    mining_tasks = relationship("MiningTaskModel", back_populates="account")  # Link to mining tasks
    wallets = relationship("WalletModel", back_populates="account")  # Link to wallets

# Wallet model