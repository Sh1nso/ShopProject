from flask_restx import Resource, Namespace

from commans.decorators import auth_required
from commans.utils import get_username_by_jwt
from dao.model.product import ProductSchema
from implemented import product_service, user_service, bill_service, transaction_service
from setup_db import db

product_ns = Namespace('product')


@product_ns.route('/')
class ProductViews(Resource):
    @auth_required
    def get(self):
        data = product_service.get_all()
        products = ProductSchema(many=True).dump(data)
        return products, 200


@product_ns.route('/buy/<pid>')
class ProductViews(Resource):
    @auth_required
    def post(self, pid: int):
        product_cost = product_service.get_cost(pid)
        if not product_cost:
            return '', 400
        username = get_username_by_jwt()
        user = user_service.get_user_by_username(username)
        if not bill_service.check_availability_money(user.id, product_cost):
            return 'Недостаточно средств', 402
        user_bill = bill_service.get_one(user.id)
        transaction_data = {'bill_id': user_bill.id,
                            'amount': -product_cost}
        #TO DO/ SESSION TO DAO
        with db.session.begin():
            bill_service.decrease_balance(user_bill.id, product_cost)
            transaction_service.create(transaction_data)
        return 'Покупка завершена успешно!', 500