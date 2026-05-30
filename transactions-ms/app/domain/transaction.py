from dataclasses import dataclass
from datetime import datetime

@dataclass()
class Dinner:
    amount: float
    user_card: str
    restaurant_id: str
    date: datetime
