from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Set up the base class for all models
Base = declarative_base()

# Define the Category model (for types of components, e.g., Resistors, Capacitors)
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # One-to-many relationship with Product (components)
    products = relationship('Product', back_populates='category')

    def __repr__(self):
        return f"Category(id={self.id}, name={self.name})"

# Define the Product model (individual components like resistors, capacitors, etc.)
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))

    # Relationship with Category
    category = relationship('Category', back_populates='products')

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price}, quantity={self.quantity})"
