class Train:
    def __init__(self, departure, arrival, departure_time, arrival_time):
        self.departure = departure
        self.arrival = arrival
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def __str__(self):
        return f"Отправление: {self.departure}, Назначение: {self.arrival}, Время отправления: {self.departure_time}, Время прибытия: {self.arrival_time}"

    def __add__(self, other):
        if self.arrival == other.departure and self.arrival_time < other.departure_time:
            return Train(self.departure, other.arrival, self.departure_time, other.arrival_time)
        else:
            return "Невозможно совершить пересадку"


t1 = Train("Москва", "Санкт-Петербург", "08:00", "14:00")
t2 = Train("Санкт-Петербург", "Саратов", "15:00", "12:00")
t3 = Train("Саратов","Тюмень","13:00","21:00")

print(t1+t2)
print(t1+t2+t3)
print(t2+t3)
