from ..database import CreateTransactionDB
from ..models.transaction import TransactionDetails

class CreateTransactionService:
    def add_transaction(transaction: TransactionDetails) -> TransactionDetails:
        return CreateTransactionDB.add_transaction(transaction)