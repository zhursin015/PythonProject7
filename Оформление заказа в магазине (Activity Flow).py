import random

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class OrderProcessor:
    def __init__(self):
        self.cart = []
        self.customer_data = None
        self.is_paid = False

    def add_product(self, name, price):
        product = Product(name, price)
        self.cart.append(product)
        print(f"Добавлено: {name} ({price} руб.)")

    def checkout(self, address):
        if not self.cart:
            print("Корзина пуста!")
            return
        self.customer_data = address
        print(f"Оформление на адрес: {address}")
        self._process_payment()

    def _process_payment(self):
        print("Проверка оплаты...")
        # Узел принятия решения (Decision Node)
        if random.random() > 0.2:  # 80% успех
            self.is_paid = True
            print("Оплата подтверждена!")
            self._ship_order()
        else:
            print("Ошибка оплаты: недостаточно средств.")

    def _ship_order(self):
        print("Заказ собирается на складе...")
        print("Заказ передан курьеру. Спасибо за покупку!")

# --- ДЕМОНСТРАЦИЯ РАБОТЫ ---

if __name__ == "__main__":
    print("=== ТЕСТ ТАКСИ ===")
    my_taxi = TaxiOrder()
    my_taxi.select_car()
    my_taxi.confirm_order()
    my_taxi.cancel_order()  # Тест отмены
    my_taxi.select_car()    # Возврат в цикл
    my_taxi.confirm_order()
    my_taxi.car_arrive()
    my_taxi.start_trip()
    my_taxi.complete_trip()

    print("\n=== ТЕСТ МАГАЗИНА ===")
    store = OrderProcessor()
    store.add_product("Python Книга", 1200)
    store.add_product("Кофе", 300)
    store.checkout("ул. Леннона, дом 9")