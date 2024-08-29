import datetime
from typing import List

from ..config.consts import TRANSACTION_ID_DOES_NOT_EXIST, PRODUCT_ID_NOT_IN_TRANSACTION
from ..database import ReadTransactionDB
from ..exceptions import InvalidBodyException
from ..models.transaction import TransactionDetails, TransactionItemDetails
from ..utils import DateValidators

class GetSpecificTransactions:
    def get_transaction(transaction_id: int, org: str) -> TransactionDetails:
        transaction = ReadTransactionDB.get_transaction(transaction_id, org)
        if transaction is None:
            raise InvalidBodyException(TRANSACTION_ID_DOES_NOT_EXIST)
        return transaction

    def get_transaction_product(product_id: int, start_date: datetime.date, end_date: datetime.date, org: str) -> List[TransactionItemDetails]:
        DateValidators.date_difference_validator(start_date, end_date)
        transactions = ReadTransactionDB.get_transaction_items(product_id, start_date, end_date, org)
        if not transactions:
            raise InvalidBodyException(PRODUCT_ID_NOT_IN_TRANSACTION)
        return transactions