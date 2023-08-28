import ledger
from model import attendance, payments


def refresh_all(cursor):  # The event parameter is needed to handle the key press event
    attendance.refresh_dropdowns(cursor)
    payments.refresh_dropdowns(cursor)
    ledger.refresh_ledger(cursor)