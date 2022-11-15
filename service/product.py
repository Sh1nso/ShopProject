from dao.product import ProductDAO


class ProductService:
    def __init__(self, dao: ProductDAO):
        self.dao = dao

    def get_one(self, pid: int) -> ProductDAO:
        return self.dao.get_one(pid)

    def get_all(self) -> ProductDAO:
        return self.dao.get_all()

    def get_product_by_title(self, title: str) -> ProductDAO:
        return self.dao.get_product_by_title(title)

    def create(self, product_d: dict) -> ProductDAO:
        return self.dao.create(product_d)

    def delete(self, pid: int):
        return self.dao.delete(pid)

    def update_product(self, pid, product_d: dict):
        title = product_d.get('title', None)
        description = product_d.get('description', None)
        cost = product_d.get('cost', None)
        product = self.get_one(pid)
        if product is not None:
            if title is not None:
                product.title = title
            if description is not None:
                product.description = description
            if cost is not None:
                product.cost = cost
            return self.dao.update(product)
        return False

    def get_cost(self, pid: int):
        return self.dao.get_cost(pid)
