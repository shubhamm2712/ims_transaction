from typing import List, Dict

from ..config.consts import ORG, ORG_NOT_FOUND
from ..exceptions import UnauthorizedException
from ..models.transaction import TransactionDetails

def set_org_model(transaction: TransactionDetails, auth_result: Dict) -> TransactionDetails:
    if ORG in auth_result:
        transaction.org = auth_result[ORG]
        for item in transaction.items:
            item.org = auth_result[ORG]
    else:
        raise UnauthorizedException(ORG_NOT_FOUND)
    return transaction