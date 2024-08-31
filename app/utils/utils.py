from datetime import date
from typing import List, Dict, Union

from ..config.consts import ORG, ORG_NOT_FOUND, BUY, SELL
from ..exceptions import UnauthorizedException
from ..models.transaction import TransactionDetails, Transaction, TransactionItemDetails, Portfolio

def set_org_model(transaction: TransactionDetails, auth_result: Dict) -> TransactionDetails:
    if ORG in auth_result:
        transaction.org = auth_result[ORG]
        for item in transaction.items:
            item.org = auth_result[ORG]
    else:
        raise UnauthorizedException(ORG_NOT_FOUND)
    return transaction

def list_to_portfolio(start_date: date, end_date: date, transactions: List[Union[Transaction, TransactionItemDetails]]) -> Portfolio:
    buyAmount = 0
    sellAmount = 0
    for transaction in transactions:
        if type(transaction) == Transaction:
            if transaction.buyOrSell == BUY:
                buyAmount += transaction.totalAmount
            elif transaction.buyOrSell == SELL:
                sellAmount += transaction.totalAmount
        elif type(transaction) == TransactionItemDetails:
            if transaction.transaction.buyOrSell == BUY:
                buyAmount += transaction.quantity*transaction.rate
            elif transaction.transaction.buyOrSell == SELL:
                sellAmount += transaction.quantity*transaction.rate
    return Portfolio(
        buyAmount=buyAmount,
        sellAmount=sellAmount,
        startDate=start_date,
        endDate=end_date,
        transactionsList=transactions
    )