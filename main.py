"""Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента
и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль,
и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию).
"""
from pprint import pprint

def introspection_info(obj_):
    """Функция добавляет в словарь информацию, т.е. имя и тип объекта,
     список доступных атрибутов и методов."""
    info = {}
    if hasattr(obj_, '__name__'):        # если объект obj имеет атрибут __name__
        info['name'] = obj_.__name__     # добавим в словарь
    info['type'] = type(obj_).__name__   # добавим в словарь тип атрибута

    attributes = [attribute
                  for attribute in dir(obj_)                     # генерация списка атрибутов объекта
                  if not callable(getattr(obj_, attribute))]     # если объект не является методом
    info['attributes'] = attributes

    methods = [method for method in dir(obj_)                    # генерация списка методов объекта
               if callable(getattr(obj_, method))]               # если объект является вызываемым методом
    info['methods'] = methods

    info['module'] = getattr(obj_, '__module__', __name__)   # добавляем в словарь значение атрибута __module__

    return info

def show_info(obj_):
    """Функция выводит в консоль доступную информацию об объекте """
    print(f'\n{'-' * 20} {type(obj_)} {'-' * 20}\n')
    number_info = introspection_info(obj_)
    pprint(number_info)

class MyClass:
    """Тестовый класс"""
    def __init__(self, *arg):
        self.value = arg

    def one_method(self):
        pass


objects = [42, (1, 2, 3), abs, [1, 2, 3], list, sorted, MyClass, MyClass(10)]   # список тестовых объектов
for obj in objects:     # в цикле выведем информацию об объекте в консоль
    show_info(obj)
