from pydantic import BaseModel


class OrderCreate(BaseModel):
    product_id: int
    quantity: int


class Order(OrderCreate):
    id: int
    total_price: float
