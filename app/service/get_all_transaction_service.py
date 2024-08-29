from datetime import date
from typing import List

from ..config.consts import ORG, BUY_OR_SELL, BUY, SELL, CUSTOMER_ID
from ..database import ReadTransactionDB
from ..models.transaction import Transaction
from ..utils import DateValidators

class GetAllTransactions:
    def get_all_transactions(start_date: date, end_date: date, org: str) -> List[Transaction]:
        DateValidators.date_difference_validator(start_date, end_date)
        params = {
            ORG: org
        }
        return ReadTransactionDB.get_transactions(start_date, end_date, params)

    def get_transactions_buy(start_date: date, end_date: date, org: str) -> List[Transaction]:
        DateValidators.date_difference_validator(start_date, end_date)
        params = {
            ORG: org,
            BUY_OR_SELL: BUY
        }
        return ReadTransactionDB.get_transactions(start_date, end_date, params)

    def get_transactions_sell(start_date: date, end_date: date, org: str) -> List[Transaction]:
        DateValidators.date_difference_validator(start_date, end_date)
        params = {
            ORG: org,
            BUY_OR_SELL: SELL
        }
        return ReadTransactionDB.get_transactions(start_date, end_date, params)
    
    def get_transaction_customer(customer_id: int, start_date: date, end_date: date, org: str) -> List[Transaction]:
        DateValidators.date_difference_validator(start_date, end_date)
        params = {
            ORG: org,
            CUSTOMER_ID: customer_id
        }
        return ReadTransactionDB.get_transactions(start_date, end_date, params)