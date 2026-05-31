from abc import ABC, abstractmethod
from transactions_ms.app.domain.Transaction import Transaction

class TransactionPublisher(ABC):

    @abstractmethod
    def publish(self, transaction: Transaction):
        pass
