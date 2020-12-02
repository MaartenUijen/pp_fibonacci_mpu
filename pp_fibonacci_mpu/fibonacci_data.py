from typing import List
from pp_fibonacci_mpu.pp_fibonacci_mpu.fibonacci_cache import memoize


class FibonacciData:

    def __init__(self):
        self.look_up_table = {0: 0, 1: 1}

    @memoize
    def add_fibonacci_number(self, n: int) -> int:
        """ Recursion method of the n-th fibonacci number.
        Checks first if its available in the cache. If not,
        adds to cache and returns the n-th fibonacci number"""
        if n < 0:
            return -1
        if n == 0 or n == 1:
            return n
        else:
            next_fib = self.add_fibonacci_number(n - 1) + self.add_fibonacci_number(n - 2)
            return next_fib

    def build_sequence(self, n: int) -> List[int]:
        """Returns list of fibonacci numbers until the n-th fibonacci number."""
        if n < 0:
            return [-1]
        else:
            sequence = [self.add_fibonacci_number(i) for i in range(n + 1)]
            return sequence

    def update_look_up_table(self, number: int) -> None:
        """Updates the look_up_table with key=Fibonacci number, value = index"""
        if number < 2:
            self.look_up_table[number] = - 1
        next_fib = 1
        index = 2
        while next_fib < number:
            index += 1
            next_fib = self.add_fibonacci_number(index)
            self.look_up_table[next_fib] = index
        if number is not next_fib:
            index = self.get_closest_index(index, number,
                                           self.add_fibonacci_number(index - 1),
                                           self.add_fibonacci_number(index))
            self.look_up_table[number] = index

    def search_index_fibonacci_number(self, number: int) -> int:
        """Returns an index corresponding to the given fibonacci number."""
        if self.look_up_table.get(number) is not None:
            return self.look_up_table[number]
        else:
            self.update_look_up_table(number)
            return self.look_up_table[number]

    @staticmethod
    def get_closest_index(index: int, number: int, previous: int, current: int) -> int:
        """Helper function. Gives back the index of the nearest fibonacci number"""
        if abs(previous - number) <= abs(current - number):
            return index - 1
        else:
            return index
