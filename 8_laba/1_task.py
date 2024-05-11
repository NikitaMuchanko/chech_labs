class New():
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def print_numbers(self):
        print(f"Первое число {self.n1} , вторая переменная {self.n2}")

    def change_numbers(self, new_n1, new_n2):
        self.n1 = new_n1
        self.n2 = new_n2

    def sum_numbers(self):
        return self.n1 + self.n2
    
    def max_numbers(self):
        return max(self.n1, self.n2)
    

a = New(5,16)
a.print_numbers()
a.change_numbers(20, 30)
a.print_numbers()
print(a.sum_numbers())
print(a.max_numbers())