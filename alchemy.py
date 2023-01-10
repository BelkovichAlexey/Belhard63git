from sqlalchemy import create_engine, select, or_, all_, and_, delete, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker, Session

from models import Category, Product, User, Status, Order, Order_item


# product = Product.get(1)
# product.description='warm'
# product.category_id= 3
# product.save()

#
# product = Product(title='Cake', description='good', category_id=2)
# product.save()

# engine = create_engine('postgresql://alexey:1234@localhost:5432/bh63')
# _Session = sessionmaker(bind=engine)

# with _Session() as session:
#     category = Category(name='Drinks')
#     session.add(category)
#     session.commit()
#     session.refresh(category)
#     print(category.id)

# with _Session() as session:
# #     category = session.get(Category, 1)
# #     print(category.__dict__)
#     categories = session.scalars(
#         select(Category).filter_by(name='Food')
#     )
#     print(categories.all())
#
# with _Session() as session:
#     products = [
#         {
#             'title': 'food1',
#             'description': 'cold1',
#             'category_id': '1'
#         },
#         {
#             'title': 'food2',
#             'description': 'cold2',
#             'category_id': '1'
#         }, {
#             'title': 'food3',
#             'description': 'cold3',
#             'category_id': '1'
#         }, {
#             'title': 'food4',
#             'description': 'cold4',
#             'category_id': '1'
#         }, {
#             'title': 'food5',
#             'description': 'cold5',
#             'category_id': '1'
#         }
#     ]
# for product in products:
#     product = Product(**product)
#     session.add(product)
#     try:
#         session.commit()
#     except IntegrityError:
#         pass
#
# with _Session() as session:
#     response = session.execute(
#         select(Category, Product)
#         .join(Product, Category.id == Product.category_id)
#     )
#     for category, product in response.all():
#         print (category.name, product.title)

# with _Session() as session:
#     product = session.get(Product,17)  # удаление об.екта одного
#     session.delete(product)
#     session.commit()
    # session.execute(delete(Product).where(Product.id ==18)) # удаление с условиемб выборка
    # session.commit()

# with _Session() as session:
#     # session.execute(
#     #     update(Category)
#     #     .where(Category.id == 2)
#     #     .values(name='Banana')
#     # )
#     # session.commit()
#
#     category = session.get(Category, 1)
#     category.name = 'fanta'
#     session.add(category)
#     session.commit()
#




