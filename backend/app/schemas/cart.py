from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal

class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Product id")
    quantity: int = Field(..., gt=0, description="Quantity")

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="Product id")
    quantity: int = Field(..., gt=0, description="New quantity")

class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description='Product name')
    price: Decimal = Field(..., description='Product price')
    quantity: int = Field(..., gt=0, description="Quantity in cart")
    subtotal: Decimal = Field(..., description='Total price (price * quantity)')
    image_url: Optional[str] = Field(None, description="Product image URL")
    
class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description="List of items in the cart")
    total: Decimal = Field(..., description="Total cart price")
    items_count: int = Field(..., description="Total number of items in the cart")