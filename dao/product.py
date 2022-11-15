from dao.model.product import Product


class ProductDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid: int) -> Product:
        return self.session.query(Product).get(uid)

    def get_all(self) -> Product:
        return self.session.query(Product).all()

    def get_product_by_title(self, title: str) -> Product:
        return self.session.query(Product).filter(Product.title == title).first()

    def get_cost(self, pid):
        product = self.get_one(pid)
        return int(product.cost)

    def create(self, product_d: dict) -> Product:
        product = Product(**product_d)
        self.session.add(product)
        self.session.commit()
        return product

    def delete(self, pid: int) -> str:
        product = self.get_one(pid)
        self.session.delete(product)
        self.session.commit()
        return product

    def update(self, product):
        self.session.add(product)
        self.session.commit()
        return product
