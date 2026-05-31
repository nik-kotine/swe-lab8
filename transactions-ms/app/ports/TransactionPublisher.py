from abc import ABC, abstractmethod
from app.domain.Transaction import Transaction

class TransactionPublisher(ABC):

    @abstractmethod
    def publish(self, transaction: Transaction):
        pass
