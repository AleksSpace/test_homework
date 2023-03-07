import unittest

from .main import shaff


class TestShaff(unittest.TestCase):

    def test_shaff(self):
        """Тест на то что изначальный список не равен возвращённому из функции"""
        arr = [3, 6, 13, 2, 7, 9]
        copy_arr = arr.copy()
        new_arr = shaff(arr)

        self.assertNotEqual(new_arr, copy_arr)  # Изначальный список не равен тому что вернула функция
        self.assertNotEqual(new_arr, shaff(copy_arr))  # Функция всегда возвращает новый список
