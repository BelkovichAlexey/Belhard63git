from sqlalchemy import Column, VARCHAR, INT, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, Session, sessionmaker, create_session

Base = declarative_base()


class BaseMixin:
    id = Column(INT, primary_key=True)

    engine = create_engine('postgresql://alexey:1234@localhost:5432/bh63')
    Session = sessionmaker(bind=engine)

    def save(self):
        with self.Session() as session:
            session.add(self)
            session.commit()
            session.refresh(self)

    @classmethod
    def get(cls, pk):
        with cls.Session() as session:
            return session.get(cls, pk)


class Category(BaseMixin, Base):
    __tablename__ = 'categories'

    name = Column(VARCHAR(24), nullable=False, unique=True)


class User(BaseMixin, Base):
    __tablename__ = 'users'

    name = Column(VARCHAR(24), nullable=False)
    email = Column(VARCHAR(24), nullable=False, unique=True)


class Status(BaseMixin, Base):
    __tablename__ = 'statuses'

    name = Column(VARCHAR(10), unique=True, nullable=False)


#
class Product(BaseMixin, Base):
    __tablename__ = 'products'

    title = Column(VARCHAR(36), nullable=False)
    description = Column(VARCHAR(140), nullable=False)
    category_id = Column(INT, ForeignKey('categories.id'), nullable=False)


class Order(BaseMixin, Base):
    __tablename__ = 'orders'

    user_id = Column(INT, ForeignKey('users.id'), nullable=False)
    status_id = Column(INT, ForeignKey('statuses.id'), nullable=False)


class Order_item(BaseMixin, Base):
    __tablename__ = 'order_items'

    order_id = Column(INT, ForeignKey('orders.id'), nullable=False)
