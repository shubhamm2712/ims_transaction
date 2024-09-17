## Routes
PATH_PREFIX_TRANSACTION = "/transactions"

# Transaction Routes
class TransactionRoutes:
    ADD_TRANSACTION = "/add_transaction"
    GET_TRANSACTION = "/get_transaction"
    GET_ALL_TRANSACTIONS = "/get_all_transactions"
    GET_TRANSACTION_CUSTOMER = "/get_transaction_customer"
    GET_TRANSACTION_PRODUCT = "/get_transaction_product"
    GET_TRANSACTION_BUY = "/get_transaction_buy"
    GET_TRANSACTION_SELL = "/get_transaction_sell"

# Config file
CONFIG_FILE = ".env"

# Logger
LOG_FILE = "app/app.log"

# Databases
DB_ECHO = False
DB_NAME = "imstransaction"

# Service
ROUNDING_FACTOR = 4

# EXCEPTIONS
INVALID_TRANSACTION_DETAILS_TYPE = "Invalid transaction details type"
INVALID_TRANSACTION_DETAILS_DO_NOT_MATCH = "Invalid transaction details do not match"
INVOICE_NOT_FOUND = "Invoice Number not found"
ORG_NOT_FOUND = "Org not found"
INVALID_DATE_PASSED = "Invalid date passed"
INVALID_DATE_RANGE_PASSED = "Invalid date range passed"
TRANSACTION_ID_DOES_NOT_EXIST = "Transaction ID does not exist"
PRODUCT_ID_NOT_IN_TRANSACTION = "Product ID is not present in any transactions in this date range"

# BUY_OR_SELL
BUY = "BUY"
SELL = "SELL"

# MODEL
ORG = "org"
BUY_OR_SELL = "buyOrSell"
CUSTOMER_ID = "customerId"