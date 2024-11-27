"""Задача "Логирование бегунов":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
Основное обновление - выбрасывание исключений, если передан неверный тип в name и если передано отрицательное значение в speed.

Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:
Уровень - INFO
Режим - запись с заменой('w')
Название файла - runner_tests.log
Кодировка - UTF-8
Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.

Дополните методы тестирования в классе RunnerTest следующим образом:
test_walk:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте отрицательное значение в speed.
В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверная скорость для Runner".
test_run:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте что-то кроме строки в name.
В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверный тип данных для объекта Runner"."""
import logging  # Импортируем модуль для логирования
import unittest  # Импортируем модуль для написания тестов

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования установлен на INFO
    filename='runner_tests.log',  # Указываем имя файла для записи логов
    filemode='w',  # Режим записи с заменой (перезапись файла)
    encoding='utf-8',  # Устанавливаем кодировку файла
    format='%(levelname)s: %(message)s'  # Формат вывода логов
)

class Runner:  # Определяем класс Runner
    def __init__(self, name, speed):  # Конструктор класса с параметрами name и speed
        if not isinstance(name, str):  # Проверяем, является ли name строкой
            raise TypeError("Name must be a string")  # Если нет, выбрасываем исключение TypeError
        if speed < 0:  # Проверяем, является ли speed отрицательным
            raise ValueError("Speed must be non-negative")  # Если да, выбрасываем исключение ValueError
        self.name = name  # Сохраняем имя в атрибуте экземпляра
        self.speed = speed  # Сохраняем скорость в атрибуте экземпляра

class RunnerTest(unittest.TestCase):  # Определяем класс тестов RunnerTest, наследующий от unittest.TestCase
    def test_walk(self):  # Метод тестирования для проверки скорости
        try:
            runner = Runner("John", -5)  # Пытаемся создать объект Runner с отрицательной скоростью
        except ValueError:  # Если возникает исключение ValueError
            logging.warning("Неверная скорость для Runner")  # Логируем предупреждение об ошибке
        else:  # Если исключения нет
            logging.info('"test_walk" выполнен успешно')  # Логируем успешное выполнение теста

    def test_run(self):  # Метод тестирования для проверки имени
        try:
            runner = Runner(123, 10)  # Пытаемся создать объект Runner с неверным типом имени
        except TypeError:  # Если возникает исключение TypeError
            logging.warning("Неверный тип данных для объекта Runner")  # Логируем предупреждение об ошибке
        else:  # Если исключения нет
            logging.info('"test_run" выполнен успешно')  # Логируем успешное выполнение теста

if __name__ == '__main__':  # Проверяем, является ли данный файл основным модулем
    unittest.main()  # Запускаем тесты