from dataclasses import dataclass
from datetime import datetime

@dataclass()
class Transaction:
    user_id: str
    amount: float
    user_card: str
    restaurant_id: str
    date: datetime
