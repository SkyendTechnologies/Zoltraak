#from routers import Routering
from fastapi import Depends, HTTPException
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from models.db_helper import db_helper
from models.wallet_model import WalletModel
from models.accounts.account_model import AccountModel

Routering = APIRouter()

#
@Routering.get("/online/wallets/{wallet_address}/connect/{account_id}")
async def connect(
    wallet_address: str,
    account_id: int,
    session: AsyncSession = Depends(db_helper.get_session)
):
    """
    Endpoint to connect a wallet to an account.

    Args:
        wallet_address (str): The address of the wallet to connect.
        account_id (int): The ID of the account to connect the wallet to.
        session (AsyncSession): Database session dependency.

    Returns:
        dict: Success message with wallet address and account ID.

    Raises:
        HTTPException: If the account does not exist or wallet already exists.
    """
    # Check if account exists
    account = await session.get(AccountModel, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    # Check if wallet already exists
    wallet = await session.execute(
        session.query(WalletModel).filter(WalletModel.address == wallet_address)
    )
    if wallet.scalars().first():
        raise HTTPException(status_code=400, detail="Wallet already exists")

    # Create a new wallet
    new_wallet = WalletModel(account_id=account_id, address=wallet_address)
    session.add(new_wallet)
    await session.commit()

    return {"message": "Wallet connected successfully", "wallet_address": wallet_address, "account_id": account_id}
