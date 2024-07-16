class Jar:
    def __init__(self, capacity=12):

        if not isinstance(capacity, int) or capacity < 0: #isinstance = second evalue is instance of first
            raise ValueError("Capacity must be a non-negative integer")

        self._capacity = capacity
        self._cookies = 0 #start at 0

    def __str__(self):
        return "🍪" *self._cookies

    def deposit(self, n):
        if self._cookies + n > self._capacity:
            raise ValueError("Deposit value too large")
        self._cookies += n

    def withdraw(self, n):
        if n > self._cookies + n > self._capacity:
            raise ValueError("Withdraw value too large")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies
