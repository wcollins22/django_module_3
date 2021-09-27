class Glass:
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def pour_in(self, amount):
        self.amount += amount

    def pour_out(self, amount):
        self.amount -= amount



