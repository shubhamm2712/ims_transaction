from datetime import date
from typing import List

from ..config.consts import ORG, BUY_OR_SELL, BUY, SELL, CUSTOMER_ID
from ..database import ReadTransactionDB
from ..models.transaction import Portfolio
from ..utils import DateValidators, list_to_portfolio

class GetAllTransactions:
    def get_all_transactions(start_date: date, end_date: date, org: str) -> Portfolio:
        DateValidators.date_difference_validator(start_date, end_date)
        params = {
            ORG: org
        }
        return list_to_portfolio(start_date, end_date, ReadTransactionDB.get_transactions(start_date, end_date, params))

    def get_transactions_buy(start_date: date, end_date: date, org: str) -> Portfolio:
        DateValidators.date_difference_validator(start_date, end_date)
        params = {
            ORG: org,
            BUY_OR_SELL: BUY
        }
        return list_to_portfolio(start_date, end_date, ReadTransactionDB.get_transactions(start_date, end_date, params))

    def get_transactions_sell(start_date: date, end_date: date, org: str) -> Portfolio:
        DateValidators.date_difference_validator(start_date, end_date)
        params = {
            ORG: org,
            BUY_OR_SELL: SELL
        }
        return list_to_portfolio(start_date, end_date, ReadTransactionDB.get_transactions(start_date, end_date, params))
    
    def get_transaction_customer(customer_id: int, start_date: date, end_date: date, org: str) -> Portfolio:
        DateValidators.date_difference_validator(start_date, end_date)
        params = {
            ORG: org,
            CUSTOMER_ID: customer_id
        }
        return list_to_portfolio(start_date, end_date, ReadTransactionDB.get_transactions(start_date, end_date, params))
