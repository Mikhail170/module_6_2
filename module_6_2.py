class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner):
        self.owner = owner
        self.__model = 'Toyota Mark II'
        self.__engine_power = 500
        self.__color = 'blue'

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(vehicle1.get_model() + '\n' + vehicle1.get_horsepower()
              + '\n' + vehicle1.get_color() + '\n' + f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5

    def __init__(self, owner, model, horsepower, color):
        super().__init__(owner)


vehicle1 = Vehicle('Fedos')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
