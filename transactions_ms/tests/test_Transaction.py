from datetime import datetime
from transactions_ms.app.domain.Transaction import Transaction

def test_TransactionShouldStoreFields():
    date = datetime.now()
    transaction = Transaction(
        user_id="JOHNID",
        amount=100,
        user_card="CARD123",
        restaurant_id="R001",
        date=date
    )

    assert transaction.user_id == "JOHNID"
    assert transaction.amount == 100
    assert transaction.user_card == "CARD123"
    assert transaction.restaurant_id == "R001"
    assert transaction.date == date
