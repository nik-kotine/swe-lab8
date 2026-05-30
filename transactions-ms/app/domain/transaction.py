from dataclasses import dataclass
from datetime import datetime

@dataclass()
class Dinner:
    amount: float
    user_card: str
    restaurant_id: str
    date: datetime

    def __init__(self, _amount: float, _user_card: str, _restaurant_id: str):
        self.amount = _amount
        self.user_card = _user_card
        self.restaurant_id = _restaurant_id
        self.date = datetime.now()
