from dataclasses import dataclass
from enum import Enum

class FuelTypes(Enum):
    PETROL = "Бензин"
    DIESEL = "Дизель"
    ELECTRO = "Электричество"


@dataclass
class HorsePower:
    value: int

    def __post_init__(self) -> None:
        if self.value < 1 or 200 < self.value:
            raise ValueError(f'Неверное число лошадиных сил: {self.value}')


class Engine:
    """
    Класс, представляющий двигатель автомобиля.
    """

    def __init__(self, horse_power: HorsePower, fuel_type: FuelTypes) -> None:
        """
        Создание и подготовка к работе объекта класса Engine (Двигатель)

        :param horse_power: HorsePower: Мощность двигателя в лошадиных силах.
        :param fuel_type: str: Тип топлива.
        """
        self.horsepower: HorsePower = horse_power
        self.fuel_type: FuelTypes = fuel_type

    def __str__(self) -> str:
        """
        Строковое представление объектов класса Engine (Двигатель).

        :return: str: Строковое представление объектов класса Engine (Двигатель).
        """
        return f'Мощность: {self.horsepower.value} л/с | Тип топлива: {self.fuel_type}'

    def change_fuel_type(self, new_fuel_type: FuelTypes) -> FuelTypes:
        """
        Изменяет тип топлива двигателя.

        :param new_fuel_type: str: Новый тип топлива.
        :return: HorsePower: Измененный тип топлива.
        :raises ValueError: Если текущий тип топлива или новый - "Электричество".

        >>> test_engine = Engine(HorsePower(150), FuelTypes.PETROL)
        >>> test_engine.change_fuel_type(FuelTypes.DIESEL)
        <FuelTypes.DIESEL: 'Дизель'>
        >>> test_engine.change_fuel_type(FuelTypes.ELECTRO)
        Traceback (most recent call last):
        ...
        ValueError: Нельзя сменить тип топлива на электричество
        """
        if self.fuel_type == FuelTypes.ELECTRO or new_fuel_type == FuelTypes.ELECTRO:
            raise ValueError("Нельзя сменить тип топлива на электричество")
        self.fuel_type = new_fuel_type
        return self.fuel_type


class CarBody:
    """
    Класс, представляющий кузов автомобиля.
    """

    def __init__(self, car_body: str, door: int) -> None:
        """
        Создание и подготовка к работе объекта класса CarBody (Кузов автомобиля).

        :param car_body: str: Тип кузова (например, седан, хэтчбек, внедорожник).
        :param door: int: Количество дверей.
        """
        self.car_body: str = car_body
        self.door: int = door

class Wheel:
    """
    Класс, представляющий колеса автомобиля.
    """

    def __init__(self, diameter: int, rubber: str) -> None:
        """
        Создание и подготовка к работе объекта класса Wheel (Колеса автомобиля).

        :param diameter: int: Диаметр колеса.
        :param rubber: str: Тип резины.
        """
        self.diameter: int = diameter
        self.rubber: str = rubber

class Car:
    """
    Класс, представляющий автомобиль
    """

    def __init__(self, horsepower: HorsePower, fuel_type: FuelTypes, car_body: str, door: int) -> None:
        """
        Создание и подготовка к работе объекта класса Car (автомобиль).

        :param horsepower: HorsePower: Мощность двигателя в лошадиных силах.
        :param fuel_type: str: Тип топлива.
        :param car_body: str: Тип кузова (например, седан, хэтчбек, внедорожник).
        :param door: int: Количество дверей.
        """
        self.engine: Engine = Engine(horsepower, fuel_type)
        self.car_body: CarBody = CarBody(car_body, door)
        self.wheel = []

    def add_wheel(self, diameter: int, rubber: str) -> None:
        """
        Добавляет диаметр и тип резины колес в объект класса Car (автомобиль).

        :param diameter: int: Диаметр колеса.
        :param rubber: str: Тип резины.
        """
        self.wheel.append(Wheel(diameter, rubber))

    def display_engine_info(self) -> str:
        """
        Выводит максимальную мощность и тип топлива автомобиля

        :return: str: мощность и тип топлива.
        """
        return (f'максимальная мощность (в л/с): {self.engine.horsepower.value}'
                f'\nтип топлива: {self.engine.fuel_type.value}')

    def display_car_body_info(self) -> str:
        """
        Выводит тип кузова и количество дверей автомобиля

        :return: str: тип кузова и количество дверей.
        """
        return (f'тип кузова: {self.car_body.car_body}'
                f'\nколичество дверей: {self.car_body.door}')

    def display_wheel_info(self) -> str:
        """
        Выводит диаметр колес и тип резины автомобиля
        :return:
        :raises ValueError: В автомобиле должно быть 4 колеса, проверьте добавленную информацию.
        """
        if not len(self.wheel) == 4:
            #print('Проверьте количество добавленных колес, их должно быть 4 шт')
            raise ValueError("В автомобиле должно быть 4 колеса, проверьте добавленную информацию")
        diameter_set = set([self.wheel[i].diameter for i in range(len(self.wheel))])
        rubber_set = set([self.wheel[i].rubber for i in range(len(self.wheel))])
        return (f'диаметр колес: {diameter_set}'
                f'\nтип резины: {rubber_set}\n')


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Авто 1
    car1 = Car(HorsePower(120), FuelTypes.PETROL, 'сидан', 5)
    car1.add_wheel(18, 'летняя')
    car1.add_wheel(18, 'летняя')
    car1.add_wheel(18, 'летняя')
    car1.add_wheel(18, 'летняя')

    print(car1.display_engine_info())
    print(car1.display_car_body_info())
    print(car1.display_wheel_info())


    # Авто 2
    car2 = Car(HorsePower(90), FuelTypes.PETROL, 'хэтчбек', 3)
    car2.add_wheel(15, 'летняя')
    car2.add_wheel(15, 'летняя')
    car2.add_wheel(15, 'всесезонная')
    car2.add_wheel(15, 'всесезонная')

    print(car2.display_engine_info())
    print(car2.display_car_body_info())
    print(car2.display_wheel_info())


    # Авто 3
    car3 = Car(HorsePower(150), FuelTypes.DIESEL, 'внедорожник', 5)
    car3.add_wheel(20, 'повышенной проходимости')
    car3.add_wheel(20, 'повышенной проходимости')
    car3.add_wheel(20, 'повышенной проходимости')
    car3.add_wheel(20, 'повышенной проходимости')

    print(car3.display_engine_info())
    print(car3.display_car_body_info())
    print(car3.display_wheel_info())
