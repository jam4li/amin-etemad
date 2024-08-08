from fastapi import APIRouter, Depends, HTTPException
from typing import List
from apps.orders.schemas import OrderCreate, Order
from apps.orders.crud import get_orders, get_order, create_order
from apps.orders.dependencies import verify_product

router = APIRouter()


@router.get("/orders/", response_model=List[Order])
async def list_orders():
    return get_orders()


@router.get("/orders/{order_id}", response_model=Order)
async def retrieve_order(order_id: int):
    return get_order(order_id)


@router.post("/orders/", response_model=Order)
async def create_new_order(order: OrderCreate, product: dict = Depends(verify_product)):
    total_price = order.quantity * product['price']
    new_order = Order(id=len(get_orders()) + 1,
                      total_price=total_price, **order.dict())
    create_order(new_order)
    # Deduct stock from product service here
    return new_order
