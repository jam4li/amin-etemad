from typing import List
from .models import Order

orders_db = []


def get_orders() -> List[Order]:
    return orders_db


def get_order(order_id: int) -> Order:
    return next(order for order in orders_db if order.id == order_id)


def create_order(order: Order):
    orders_db.append(order)
    return order
