from sqlmodel import Session

from ..config import engine
from ..models.transaction import Transaction, TransactionDetails

class CreateTransactionDB:
    def add_transaction(transaction: Transaction) -> TransactionDetails:
        with Session(engine) as session:
            db_trans = Transaction.model_validate(transaction)
            session.add(db_trans)
            session.commit()
            session.refresh(db_trans)
            return TransactionDetails.model_validate(db_trans)