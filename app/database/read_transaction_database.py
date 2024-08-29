from datetime import date
from sqlmodel import Session, select
from typing import Optional, List, Dict

from ..config.consts import BUY_OR_SELL, ORG, CUSTOMER_ID
from ..config import engine
from ..models.transaction import Transaction, TransactionItem, TransactionDetails, TransactionItemDetails

class ReadTransactionDB:
    def get_transaction(transaction_id: int, org: str) -> Optional[TransactionDetails]:
        with Session(engine) as session:
            statement = select(Transaction).where(Transaction.id == transaction_id, Transaction.org == org)
            results = session.exec(statement)
            db_transaction = results.first()
            if db_transaction is None:
                return None
            return TransactionDetails.model_validate(db_transaction)

    def get_transaction_items(product_id: int, start_date: date, end_date: date, org: str) -> List[TransactionItemDetails]:
        with Session(engine) as session:
            statement = select(Transaction, TransactionItem).join(TransactionItem).where(TransactionItem.productId == product_id, Transaction.date >= start_date, Transaction.date <= end_date, Transaction.org == org)
            results = session.exec(statement)
            transaction_items = []
            for _, transaction_item in results.all():
                transaction_items.append(TransactionItemDetails.model_validate(transaction_item))
            return transaction_items
    
    def get_transactions(start_date: date, end_date: date, params: Dict) -> List[Transaction]:
        if ORG not in params:
            return []
        with Session(engine) as session:
            statement = select(Transaction).where(Transaction.org == params[ORG], Transaction.date >= start_date, Transaction.date <= end_date)
            if BUY_OR_SELL in params:
                statement = select(Transaction).where(Transaction.org == params[ORG], Transaction.buyOrSell == params[BUY_OR_SELL], Transaction.date >= start_date, Transaction.date <= end_date)
            elif CUSTOMER_ID in params:
                statement = select(Transaction).where(Transaction.org == params[ORG], Transaction.customerId == params[CUSTOMER_ID], Transaction.date >= start_date, Transaction.date <= end_date)
            results = session.exec(statement)
            return results.all()