from abc import ABC, abstractmethod

# Базовый класс состояния
class State(ABC):
    @abstractmethod
    def select_car(self, context): pass
    @abstractmethod
    def confirm_order(self, context): pass
    @abstractmethod
    def car_arrive(self, context): pass
    @abstractmethod
    def start_trip(self, context): pass
    @abstractmethod
    def complete_trip(self, context): pass
    @abstractmethod
    def cancel_order(self, context): pass

# Конкретные состояния
class IdleState(State):
    def select_car(self, context):
        print("Автомобиль выбран.")
        context.set_state(CarSelectedState())
    def confirm_order(self, context): print("Ошибка: сначала выберите авто.")
    def car_arrive(self, context): print("Ошибка: заказа нет.")
    def start_trip(self, context): print("Ошибка: заказа нет.")
    def complete_trip(self, context): print("Ошибка: поездка не начата.")
    def cancel_order(self, context): print("Нечего отменять.")

class CarSelectedState(State):
    def select_car(self, context): print("Авто уже выбрано.")
    def confirm_order(self, context):
        print("Заказ подтвержден. Машина выехала.")
        context.set_state(OrderConfirmedState())
    def car_arrive(self, context): print("Машина еще не выехала.")
    def start_trip(self, context): print("Рано ехать.")
    def complete_trip(self, context): print("Поездка не началась.")
    def cancel_order(self, context):
        print("Заказ отменен.")
        context.set_state(TripCancelledState())

class OrderConfirmedState(State):
    def select_car(self, context): print("Нельзя менять авто после подтверждения.")
    def confirm_order(self, context): print("Уже подтверждено.")
    def car_arrive(self, context):
        print("Машина прибыла!")
        context.set_state(CarArrivedState())
    def start_trip(self, context): print("Машина еще в пути.")
    def complete_trip(self, context): print("Еще не приехали.")
    def cancel_order(self, context):
        print("Отмена заказа. Водитель уезжает.")
        context.set_state(TripCancelledState())

class CarArrivedState(State):
    def select_car(self, context): print("Поздно менять.")
    def confirm_order(self, context): pass
    def car_arrive(self, context): print("Уже на месте.")
    def start_trip(self, context):
        print("Поездка началась!")
        context.set_state(InTripState())
    def complete_trip(self, context): pass
    def cancel_order(self, context):
        print("Отмена. Машина была у подъезда.")
        context.set_state(TripCancelledState())

class InTripState(State):
    def select_car(self, context): pass
    def confirm_order(self, context): pass
    def car_arrive(self, context): pass
    def start_trip(self, context): print("Мы уже едем.")
    def complete_trip(self, context):
        print("Приехали! Ожидание оплаты.")
        context.set_state(TripCompletedState())
    def cancel_order(self, context): print("Нельзя отменить в пути!")

class TripCompletedState(State):
    def select_car(self, context): pass
    def confirm_order(self, context): pass
    def car_arrive(self, context): pass
    def start_trip(self, context): pass
    def complete_trip(self, context): print("Уже завершено.")
    def cancel_order(self, context): print("Поздно.")

class TripCancelledState(State):
    def select_car(self, context):
        print("Начинаем поиск заново...")
        context.set_state(IdleState())
        context.select_car()
    def confirm_order(self, context): pass
    def car_arrive(self, context): pass
    def start_trip(self, context): pass
    def complete_trip(self, context): pass
    def cancel_order(self, context): print("Уже отменено.")

# Контекст
class TaxiOrder:
    def __init__(self):
        self.state = IdleState()
        print("Статус: Ожидание (Idle)")

    def set_state(self, state):
        self.state = state

    def select_car(self): self.state.select_car(self)
    def confirm_order(self): self.state.confirm_order(self)
    def car_arrive(self): self.state.car_arrive(self)
    def start_trip(self): self.state.start_trip(self)
    def complete_trip(self): self.state.complete_trip(self)
    def cancel_order(self): self.state.cancel_order(self)