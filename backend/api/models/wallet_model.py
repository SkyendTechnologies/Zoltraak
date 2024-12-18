from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from models.db_helper import db_helper

# Wallet model
class WalletModel(db_helper.Base):
    """
    Represents a wallet associated with an account in the TON ecosystem.

    Attributes:
        id (int): Unique identifier for the wallet.
        account_id (int): ID of the associated account.
        address (str): Unique wallet address in the TON network.
        balance (float): Token balance of the wallet.
        created_at (datetime): Timestamp when the wallet was created.
        account (AccountModel): The account this wallet is associated with.
    """
    __tablename__ = 'wallets'

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    address = Column(String, nullable=False, unique=True)
    balance = Column(Float, default=0.0, nullable=False, comment="Token balance of the wallet")
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    account = relationship("AccountModel", back_populates="wallets")
