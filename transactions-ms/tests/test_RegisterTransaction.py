from app.application.RegisterTransaction import RegisterTransaction
from app.ports.TransactionPublisher import TransactionPublisher
from app.domain.Transaction import Transaction

from datetime import datetime

class MockPublisher(TransactionPublisher):

    def __init__(self):
        self.transaction = None

    def publish(self, transaction):
        self.transaction = transaction

def test_RegisterTransactionShouldPublishTransaction():
    publisher = MockPublisher()
    use_case = RegisterTransaction(publisher)
    transaction = Transaction(
        user_id = "JOHNID",
        amount = 100,
        user_card = "CARD123",
        restaurant_id = "R001",
        date = datetime.now()
    )
    use_case.execute(transaction)

    assert publisher.transaction == transaction
