from pydantic import BaseModel
from typing import Optional


class Order(BaseModel):
    product_id: int
    quantity: int
    total_price: float
