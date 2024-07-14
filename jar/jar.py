class Jar:
    def __init__(self, capacity=12):
        capacity = capacity
        cookie_jar = 0

        if capacity < 1:
            raise ValueError

        cookie_jar.capacity = capacity

        return cookie_jar

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
