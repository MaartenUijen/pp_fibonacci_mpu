from typing import List
from pp_fibonacci_mpu.pp_fibonacci_mpu.fibonacci_data import FibonacciData


class FibonacciService:

    def __init__(self):
        """ Instance of Fibonacci Data"""
        self.f = FibonacciData()

    def get_fibonacci_number(self, n: int) -> int:
        """
        :param n: An index.
        :return: Fibonacci number based on index.
        """
        return self.f.add_fibonacci_number(n)

    def get_fibonacci_sequence(self, n: int) -> List[int]:
        """
        :param n: An index.
        :return: A list with fibonacci sequence until the given index.
        """
        return self.f.build_sequence(n)

    def get_fibonacci_index(self, fibonacci_number: int) -> int:
        """
        :param fibonacci_number: An arbitrary number.
        :return: The index corresponding to the fibonacci_number. If it is not a fibonacci
        number it returns an index corresponding to the closest fibonacci number.
        """
        return self.f.search_index_fibonacci_number(fibonacci_number)

