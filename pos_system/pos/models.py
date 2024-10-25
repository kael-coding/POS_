class Product:
    def __init__(self, name: str, price: float, quantity: int, image: str):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.image = image

class POS:
    TAX_RATE = 0.12  # 12% tax rate

    def __init__(self):
        self.products: dict[str, Product] = {}
        self.history: list[dict] = []

    def add_product(self, name: str, price: float, quantity: int, image: str):
        self.products[name] = Product(name, price, quantity, image)

    def edit_product(self, name: str, price: float = None, quantity: int = None, image: str = None):
        if name in self.products:
            if price is not None:
                self.products[name].price = price
            if quantity is not None:
                self.products[name].quantity = quantity
            if image is not None:
                self.products[name].image = image

    def delete_product(self, name: str):
        """Delete a product by name."""
        if name in self.products:
            del self.products[name]

    def record_sale(self, name: str, quantity: int) -> dict | None:
        if name in self.products and self.products[name].quantity >= quantity:
            product = self.products[name]
            product.quantity -= quantity
            
            # Calculate total and tax
            total = product.price * quantity
            tax = total * self.TAX_RATE
            grand_total = total + tax
            
            sale_detail = {
                'name': product.name,
                'quantity': quantity,
                'price': product.price,
                'total': total,
                'tax': tax,
                'grand_total': grand_total,
            }
            self.history.append(sale_detail)
            return sale_detail  # Return the sale detail for the receipt
        return None
