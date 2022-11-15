from flask_restx import Namespace, Resource
from flask import request

from commans.decorators import admin_required
from dao.model.product import ProductSchema
from dao.model.user import UserSchema
from implemented import product_service, user_service

admin_ns = Namespace('admin')


@admin_ns.route('/products/')
class AdminProductsView(Resource):
    @admin_required
    def get(self):
        products_data = product_service.get_all()
        products = ProductSchema(many=True).dump(products_data)
        return products, 200

    @admin_required
    def post(self):
        product_data = request.json
        product = product_service.create(product_data)
        product_schema = ProductSchema().dump(product)
        return product_schema


@admin_ns.route('/products/<pid>')
class AdminProductView(Resource):
    @admin_required
    def delete(self, pid):
        product = product_service.delete(pid)
        return f'Товар {str(product.title)} удален'

    @admin_required
    def put(self, pid):
        product_data = request.json
        product = product_service.update_product(pid, product_data)
        return f'Товар {str(product.title)} изменен'


@admin_ns.route('/users/')
class AdminUsersView(Resource):
    @admin_required
    def get(self):
        users_data = user_service.get_all()
        users = UserSchema(many=True).dump(users_data)
        return users, 200


@admin_ns.route('/users/<uid>/')
class AdminUserView(Resource):
    @admin_required
    def put(self, uid):
        user = user_service.change_active(uid)
        if user:
            return f'Статус пользователя {user.username} - {user.is_active}', 200
        return f'Пользователя с id {uid} не существует', 404
