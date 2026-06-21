from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Cart

from app.schemas import (
    CartCreate,
    CartResponse
)

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)


@router.post(
    "/add",
    response_model=CartResponse
)
def add_to_cart(
    item: CartCreate,
    db: Session = Depends(get_db)
):

    cart_item = Cart(
        user_id=item.user_id,
        product_id=item.product_id,
        quantity=item.quantity
    )

    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)

    return cart_item


@router.get(
    "/",
    response_model=list[CartResponse]
)
def get_cart(
    db: Session = Depends(get_db)
):
    return db.query(Cart).all()


@router.delete("/{cart_id}")
def delete_cart_item(
    cart_id: int,
    db: Session = Depends(get_db)
):

    item = db.query(Cart).filter(
        Cart.id == cart_id
    ).first()

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    db.delete(item)
    db.commit()

    return {
        "message": "Item removed from cart"
    }