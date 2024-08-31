from fastapi import APIRouter
from fastapi import Depends, Security

from typing import Dict, List, Optional

import datetime

from ..config import logger
from ..config.consts import PATH_PREFIX_TRANSACTION, TransactionRoutes, ORG
from ..models.transaction import Portfolio, TransactionDetails, ExceptionClass
from ..service import CreateTransactionService, GetSpecificTransactions, GetAllTransactions
from ..utils import VerifyToken, set_org_model, DateValidators, TransactionValidator

apiRouter = APIRouter(prefix=PATH_PREFIX_TRANSACTION)
auth = VerifyToken()

bad_request_responses = {
    400: {
        "description": "Error: Bad Request",
        "model": ExceptionClass
    }
}

auth_responses = {
    401: {
        "description": "Error: Unauthorized",
        "model": ExceptionClass
    },
    403: {
        "description": "Error: Forbidden",
        "model": ExceptionClass
    }
}

@apiRouter.post(TransactionRoutes.ADD_TRANSACTION, response_model=TransactionDetails, responses=auth_responses|bad_request_responses)
async def add_transaction(transaction: TransactionDetails = Depends(TransactionValidator.add_validator), auth_result: Dict = Security(auth.verify)) -> TransactionDetails:
    set_org_model(transaction, auth_result)
    logger.debug("In add_transaction:"+str(transaction))
    return CreateTransactionService.add_transaction(transaction)

@apiRouter.get(TransactionRoutes.GET_TRANSACTION + "/{transaction_id}", response_model=TransactionDetails, responses=auth_responses|bad_request_responses)
async def get_transaction(transaction_id: int, auth_result: Dict = Security(auth.verify)) -> TransactionDetails:
    logger.debug("In get_transaction:"+str(transaction_id))
    return GetSpecificTransactions.get_transaction(transaction_id, auth_result[ORG])

@apiRouter.get(TransactionRoutes.GET_ALL_TRANSACTIONS, response_model=Portfolio, responses=auth_responses)
async def get_all_transaction(start_date: Optional[datetime.date] = Depends(DateValidators.start_date_validator), end_date: Optional[datetime.date] = Depends(DateValidators.end_date_validator), auth_result: Dict = Security(auth.verify)) -> Portfolio:
    logger.debug("In get_all_transaction: start_date:"+str(start_date),",end_date:"+str(end_date))
    return GetAllTransactions.get_all_transactions(start_date, end_date, auth_result[ORG])
    
@apiRouter.get(TransactionRoutes.GET_TRANSACTION_BUY, response_model=Portfolio, responses=auth_responses)
async def get_transaction_buy(start_date: Optional[datetime.date] = Depends(DateValidators.start_date_validator), end_date: Optional[datetime.date] = Depends(DateValidators.end_date_validator), auth_result: Dict = Security(auth.verify)) -> Portfolio:
    logger.debug("In get_transaction_buy: start_date:"+str(start_date),",end_date:"+str(end_date))
    return GetAllTransactions.get_transactions_buy(start_date, end_date, auth_result[ORG])
    
@apiRouter.get(TransactionRoutes.GET_TRANSACTION_SELL, response_model=Portfolio, responses=auth_responses)
async def get_transaction_sell(start_date: Optional[datetime.date] = Depends(DateValidators.start_date_validator), end_date: Optional[datetime.date] = Depends(DateValidators.end_date_validator), auth_result: Dict = Security(auth.verify)) -> Portfolio:
    logger.debug("In get_transaction_sell: start_date:"+str(start_date),",end_date:"+str(end_date))
    return GetAllTransactions.get_transactions_sell(start_date, end_date, auth_result[ORG])
    
@apiRouter.get(TransactionRoutes.GET_TRANSACTION_CUSTOMER + "/{customer_id}", response_model=Portfolio, responses=auth_responses)
async def get_transaction_customer(customer_id: int, start_date: Optional[datetime.date] = Depends(DateValidators.start_date_validator), end_date: Optional[datetime.date] = Depends(DateValidators.end_date_validator), auth_result: Dict = Security(auth.verify)) -> Portfolio:
    logger.debug("In get_transaction_customer: customer_id:" + str(customer_id) + ",start_date:"+str(start_date),",end_date:"+str(end_date))
    return GetAllTransactions.get_transaction_customer(customer_id, start_date, end_date, auth_result[ORG])
    
@apiRouter.get(TransactionRoutes.GET_TRANSACTION_PRODUCT + "/{product_id}", response_model=Portfolio, responses=auth_responses|bad_request_responses)
async def get_transaction_product(product_id: int, start_date: Optional[datetime.date] = Depends(DateValidators.start_date_validator), end_date: Optional[datetime.date] = Depends(DateValidators.end_date_validator), auth_result: Dict = Security(auth.verify)) -> Portfolio:
    logger.debug("In get_transaction_product: product_id:" + str(product_id) + ",start_date:"+str(start_date),",end_date:"+str(end_date))
    return GetSpecificTransactions.get_transaction_product(product_id, start_date, end_date, auth_result[ORG])