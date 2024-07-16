class Jar:
    def __init__(self, capacity=12):

        if not isinstance(capacity, int) or capacity < 0: #isinstance = second evalue is instance of first
            raise ValueError("Capacity must be a non-negative integer")

        self._capacity = capacity
        self._cookies = 0 #start at 0

    def __str__(self):


    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
