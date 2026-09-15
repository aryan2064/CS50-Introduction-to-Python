class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Invalid amount of cookies")
        self.size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Invalid amount of cookies")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Invalid capacity")

        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Not enough capacity")
        if not isinstance(size, int) or size < 0:
            raise ValueError("Invalid amount of cookies")

        self._size = size
