from typing import Optional

import httpx
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float

async def get_product(product_id: int) -> Optional[Product]:
    """Fetch product from API, return None if not found."""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"https://api.shop.com/products/{product_id}",
                timeout=5.0
            )
            response.raise_for_status()
            return Product(**response.json())
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise
        except Exception:
            raise
