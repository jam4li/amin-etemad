from fastapi import Depends, HTTPException
from apps.orders.services import get_product_details


async def verify_product(product_id: int, quantity: int):
    product = await get_product_details(product_id)
    if not product or product['stock'] < quantity:
        raise HTTPException(status_code=400, detail="Insufficient stock")
    return product
