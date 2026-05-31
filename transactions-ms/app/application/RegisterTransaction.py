from app.domain.Transaction import Transaction
from app.ports.TransactionPublisher import TransactionPublisher

class RegisterTransaction:

    def __init__(self, _publisher: TransactionPublisher):
        self.publisher = _publisher

    def execute(self, transaction: Transaction):
        self.publisher.publish(transaction)
