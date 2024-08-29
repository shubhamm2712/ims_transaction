import datetime
from typing import Optional

from ..config.consts import INVALID_DATE_PASSED, INVALID_DATE_RANGE_PASSED
from ..exceptions import InvalidBodyException

class DateValidators:
    def start_date_validator(start_date: Optional[str] = None) -> datetime.date:
        if start_date is None:
            return datetime.date.today() + datetime.timedelta(days=-30)
        try:
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        except:
            raise InvalidBodyException(INVALID_DATE_PASSED)
        return start_date
    
    def end_date_validator(end_date: Optional[str] = None) -> datetime.date:
        if end_date is None:
            return datetime.date.today()
        try:
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        except:
            raise InvalidBodyException(INVALID_DATE_PASSED)
        return end_date

    def date_difference_validator(start_date: datetime.date, end_date: datetime.date) -> None:
        if start_date > end_date:
            raise InvalidBodyException(INVALID_DATE_RANGE_PASSED)