import httpx


async def get_product_details(product_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://product_service:8000/products/{product_id}/")
        if response.status_code == 200:
            return response.json()
        return None
