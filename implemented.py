from dao.bill import BillDAO
from dao.product import ProductDAO
from dao.transaction import TransactionDAO
from dao.user import UserDAO
from service.bill import BillService
from service.product import ProductService
from service.transaction import TransactionService
from service.user import UserService
from setup_db import db

user_dao = UserDAO(session=db.session)
product_dao = ProductDAO(session=db.session)
bill_dao = BillDAO(session=db.session)
transaction_dao = TransactionDAO(session=db.session)

user_service = UserService(dao=user_dao)
product_service = ProductService(dao=product_dao)
bill_service = BillService(dao=bill_dao)
transaction_service = TransactionService(dao=transaction_dao)

