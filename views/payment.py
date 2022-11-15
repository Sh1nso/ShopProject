from flask import request
from flask_restx import Namespace, Resource

from constans import SECRET_KEY
from implemented import transaction_service, bill_service
from service.payment import payment_object

payment_ns = Namespace('payment')


@payment_ns.route('/webhook/')
class PaymentView(Resource):
    def post(self):
        data = request.json
        signature = data.get('signature', None)
        transaction_id = data.get('transaction_id', None)
        user_id = data.get('user_id', None)
        bill_id = data.get('bill_id', None)
        amount = data.get('amount', None)
        if None in [signature, transaction_id, user_id, bill_id, amount]:
            return 'Неверное переданы данные', 400
        if not payment_object.check_signature(signature, SECRET_KEY, transaction_id, user_id, bill_id, amount):
            return 'Транзакция прервана', 403
        if bill_service.check_for_exist(bill_id):
            bill_service.create({'user_id': user_id})
        transaction_data = {'bill_id': data.get('bill_id'),
                            'amount': data.get('amount')}
        transaction_service.create(transaction_data)
        bill_service.increase_balance(bill_id, amount)
        return 'Баланс пополнен', 200
