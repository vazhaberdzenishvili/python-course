from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


host = 'localhost'
port = 5432
user = 'postgres'
password = '12345678'
database = 'testdb'


engine = create_engine(
    f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
)

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    quantity_in_stock = Column(Integer, nullable=False)


class CartItem(Base):
    __tablename__ = 'cart_items'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    order_date = Column(DateTime)
    total_amount = Column(Float, nullable=False)


class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_per_item = Column(Float, nullable=False)


# Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


def populate_products():
    '''  populate Products table  '''
    products = [
        Product(name='Headset', price=99.99, quantity_in_stock=60),
        Product(name='Mousepad', price=19.99, quantity_in_stock=75),
        Product(name='Laptop Stand', price=49.99, quantity_in_stock=20),
        Product(name='Mouse', price=25.00, quantity_in_stock=10)
    ]

    session.add_all(products)
    session.commit()


populate_products()
