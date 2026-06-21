from pydantic import BaseModel, EmailStr, Field


# ======================
# USER SCHEMAS
# ======================

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length=6)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True


# ======================
# PRODUCT SCHEMAS
# ======================

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float = Field(gt=0)
    stock: int = Field(ge=0)


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int

    class Config:
        from_attributes = True


class ProductUpdate(BaseModel):
    name: str
    description: str
    price: float = Field(gt=0)
    stock: int = Field(ge=0)


# ======================
# CART SCHEMAS
# ======================

class CartCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int = Field(gt=0)


class CartResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int

    class Config:
        from_attributes = True


# ======================
# ORDER SCHEMAS
# ======================

class OrderCreate(BaseModel):
    user_id: int
    total_amount: float = Field(gt=0)


class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_amount: float
    created_at: str

    class Config:
        from_attributes = True