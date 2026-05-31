from dataclasses import dataclass

@dataclass
class TransactionReceived:
    amount: float
    user_id: str
