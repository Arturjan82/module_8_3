
class Car:
    def __init__(self, model,  __vin, __numbers):
        self.model = model
        self.__vin =  __vin
        self.__numbers = __numbers
        Car.__is_valid_vin(self.__vin)
        Car.__is_valid_numbers(self.__numbers)

    def __is_valid_vin(vin_number):
        result = False
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif vin_number >= 1000000 and vin_number <= 9999999:
            result = True
        else:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return result

    def  __is_valid_numbers(numbers):
        result = False
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers) == 6:
            result = True
        else:
            raise IncorrectCarNumbers('Неверная длина номера')
        return result

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')