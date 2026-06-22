from fastapi import FastAPI
import time

from app.database import engine
from app.database import Base

from app import models

from app.routers import users
from app.routers import products
from app.routers import cart
from app.routers import orders

# Wait for PostgreSQL container to start
time.sleep(15)

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-Commerce Backend"
)

app.include_router(users.router)
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(orders.router)