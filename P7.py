import random
engine_types = ['Petrol', 'Diesel']
engine_info = {
                'Petrol':{'max_race':200000, 'fuel_rate':8, 'dif_price':100, 'fuel_cost':2.4},
                'Diesel':{'max_race':150000, 'fuel_rate':6, 'dif_price':120, 'fuel_cost':1.8}
               }

class Race():
    def __init__(self, min_race=29000, max_race=186000):
        #self.__race = 0
        self.__min_race = min_race
        self.__max_race = max_race
    def gen_race(self):
        return random.randint(self.__min_race, self.__max_race)

class Plant():
    __count = 0
    def __init__(self):
        pass
    def create_car(self):
        self.__class__.__count+= 1
        num =  self.__class__.__count
        if self.__count % 3 == 0:
            engine_type = 'Diesel'
        else:
            engine_type = 'Petrol'
        if self.__count % 5 == 0:
            tank = 75
        else:
            tank = 60
        car = Car(num,engine_type, tank, price=10000)
        return car

class Car(object):
     def __init__(self, num, engine_type,tank, price):
         self.__number = num
         self.__price = price
         self.__engine_type = engine_type
         self.__max_race = engine_info[self.__engine_type]['max_race']
         self.__fuel_rate = engine_info[self.__engine_type]['fuel_rate']
         self.__dif_price = engine_info[self.__engine_type]['dif_price']
         self.__fuel_cost = engine_info[self.__engine_type]['fuel_cost']
         self.__tank = tank
         self.__race =  0 # self.set_race(0)
         self.__value = price
         self.__used_fuel = 0
         self.__remain_race = self.__max_race
         self.__costs = 0

     def __str__(self):
         s = 'N={}  engine_type={} value ={} used_fuel={} remain_rate={}'.\
             format(str(self.__number), self.__engine_type, str(self.__value), str(self.__used_fuel), str(self.__remain_race))
         return s

     def get_race(self):
         return self.__race
     def set_race(self, race):
         self.__race += race
         if self.__race > self.__max_race:
             self.__race = self.__max_race
         self.set_value()
         self.set_used_fuel()
         self.set_remain_race()
     race = property(get_race, set_race)

     def set_value(self):
         self.__value =  int(self.__price) - int(self.__race) * int(self.__dif_price)/ 1000
         if self.__value < 0:
             self.__value = 0
     def get_value(self):
         return self.__value
     value = property(get_value)

     def set_used_fuel(self):
         self.__used_fuel = int(self.__race) * int(self.__fuel_rate) / 100
     def get_used_fuel(self):
         return self.__used_fuel
     used_fuel = property(get_used_fuel)

     def set_remain_race(self):
         self.__remain_race = self.__max_race - self.__race
     def get_remain_race(self):
         return self.__remain_race
     remain_race = property(get_remain_race)

     def get_number(self):
         return self.__number
     def get_type(self):
         return self.__engine_type

     def __lt__(self, other):
         if self.__engine_type == 'Petrol' and other.__engine_type == 'Petrol':
             return self.__remain_race < other.__remain_race
         elif self.__engine_type == 'Diesel' and other.__engine_type == 'Diesel':
             return self.__value < other.__value
         else:
             return self.__engine_type < other.__engine_type

if __name__ == '__main__':
    plant = Plant()
    race = Race()
    cars = [plant.create_car() for i in range(30)]
    for car in cars:
        car.set_race(race.gen_race())
        print(car)

    b = sorted(cars)
    for i in b:
         print(i)

