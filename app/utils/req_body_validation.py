from datetime import date

from ..config.consts import INVALID_TRANSACTION_DETAILS_TYPE, BUY, SELL, ROUNDING_FACTOR, INVALID_TRANSACTION_DETAILS_DO_NOT_MATCH, INVOICE_NOT_FOUND
from ..exceptions import InvalidBodyException
from ..models.transaction import Transaction, TransactionDetails, TransactionItem

class TransactionValidator:
    def sanitize_trannsaction(transaction: Transaction):
        if transaction.id is not None:
            raise InvalidBodyException(INVALID_TRANSACTION_DETAILS_TYPE)
        if transaction.invoiceNumber is not None:
            if type(transaction.invoiceNumber) != str:
                raise InvalidBodyException(INVALID_TRANSACTION_DETAILS_TYPE)
            else:
                transaction.invoiceNumber = transaction.invoiceNumber.strip()
                if transaction.invoiceNumber == "":
                    raise InvalidBodyException(INVOICE_NOT_FOUND)
        if transaction.date is not None:
            if type(transaction.date) != date:
                raise InvalidBodyException(INVALID_TRANSACTION_DETAILS_TYPE)
        if transaction.description is not None:
            if type(transaction.description) != str:
                raise InvalidBodyException(INVALID_TRANSACTION_DETAILS_TYPE)
            else:
                transaction.description = transaction.description.strip()
                if transaction.description == "":
                    transaction.description = None
        if transaction.metaData is not None:
            if type(transaction.metaData) != str:
                raise InvalidBodyException(INVALID_TRANSACTION_DETAILS_TYPE)
            else:
                transaction.metaData = transaction.metaData.strip()
                if transaction.metaData == "":
                    transaction.metaData = None
        if transaction.customerId is not None:
            if type(transaction.customerId) != int:
                raise InvalidBodyException(INVALID_TRANSACTION_DETAILS_TYPE)
        if transaction.totalAmount is not None:
            if type(transaction.totalAmount) != float and type(transaction.totalAmount) != int:
                raise InvalidBodyException(INVALID_TRANSACTION_DETAILS_TYPE)
            else:
                transaction.totalAmount = round(transaction.totalAmount, ROUNDING_FACTOR)
        if transaction.buyOrSell is not None:
            if type(transaction.buyOrSell) != str:
                raise InvalidBodyException(INVALID_TRANSACTION_DETAILS_TYPE)
            else:
                transaction.buyOrSell = transaction.buyOrSell.strip()
                transaction.buyOrSell = transaction.buyOrSell.upper()
                if transaction.buyOrSell is not None and transaction.buyOrSell not in {BUY, SELL}:
                    raise InvalidBodyException(INVALID_TRANSACTION_DETAILS_TYPE)

    def sanitize_transaction_item(transaction_item: TransactionItem):
        if transaction_item.id is not None:
            raise InvalidBodyException(INVALID_TRANSACTION_DETAILS_TYPE)
        if transaction_item.transactionId is not None:
            raise InvalidBodyException(INVALID_TRANSACTION_DETAILS_TYPE)
        if transaction_item.productId is not None:
            if type(transaction_item.productId) != int:
                raise InvalidBodyException(INVALID_TRANSACTION_DETAILS_TYPE)
        if transaction_item.quantity is not None:
            if type(transaction_item.quantity) != float and type(transaction_item.quantity) != int:
                raise InvalidBodyException(INVALID_TRANSACTION_DETAILS_TYPE)
        if transaction_item.rate is not None:
            if type(transaction_item.rate) != float and type(transaction_item.rate) != int:
                raise InvalidBodyException(INVALID_TRANSACTION_DETAILS_TYPE)

    def add_validator(transaction: TransactionDetails):
        TransactionValidator.sanitize_trannsaction(transaction)
        if transaction.date is None or transaction.customerId is None or transaction.totalAmount is None or transaction.buyOrSell is None or transaction.invoiceNumber is None:
            raise InvalidBodyException(INVALID_TRANSACTION_DETAILS_TYPE)
        total_amount = 0
        for item in transaction.items:
            TransactionValidator.sanitize_transaction_item(item)
            if item.productId is None or item.quantity is None or item.rate is None:
                raise InvalidBodyException(INVALID_TRANSACTION_DETAILS_TYPE)
            total_amount += item.quantity*item.rate
        if round(total_amount, ROUNDING_FACTOR) != transaction.totalAmount:
            raise InvalidBodyException(INVALID_TRANSACTION_DETAILS_DO_NOT_MATCH)
        return transaction