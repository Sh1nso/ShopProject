from Crypto.Hash import SHA1


class PaymentService:

    def create_signature(self, private_key, transaction_id, user_id, bill_id, amount):
        signature = SHA1.new(f'{private_key}:{transaction_id}:{user_id}:{bill_id}:{amount}'.encode()).hexdigest()
        return signature

    def check_signature(self, signature, private_key, transaction_id, user_id, bill_id, amount):
        if self.create_signature(private_key, transaction_id, user_id, bill_id, amount) != signature:
            return False
        return True


payment_object = PaymentService()
