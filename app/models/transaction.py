import datetime

from typing import Optional, List, Union
from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel

class TransactionBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    org: Optional[str] = None
    invoiceNumber: Optional[str] = None 
    date: Optional[datetime.date] = None
    description: Optional[str] = None
    metaData: Optional[str] = None
    customerId: Optional[int] = None
    totalAmount: Optional[float] = None
    buyOrSell: Optional[str] = None

class Transaction(TransactionBase, table=True):
    items: List["TransactionItem"] = Relationship(back_populates="transaction")

class TransactionItemBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    org: Optional[str] = None
    productId: Optional[int] = None
    quantity: Optional[float] = None
    rate: Optional[float] = None

    transactionId: Optional[int] = Field(default=None, foreign_key="transaction.id")

class TransactionItem(TransactionItemBase, table=True):
    transaction: Optional["Transaction"] = Relationship(back_populates="items")

class TransactionDetails(TransactionBase):
    items: List["TransactionItem"] = []

class TransactionItemDetails(TransactionItemBase):
    transaction: Optional["Transaction"] = None

class Portfolio(BaseModel):
    buyAmount: Optional[float] = None
    sellAmount: Optional[float] = None
    startDate: Optional[datetime.date] = None
    endDate: Optional[datetime.date] = None

    transactionsList: List[Union[Transaction, TransactionItemDetails]] = []

class ExceptionClass(BaseModel):
    detail: str