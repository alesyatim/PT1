import random
engine_types = ['Petrol', 'Diesel']
engine_info = {
                engine_types[0]:{'race':200000, 'fuel_rate':8, 'dif_price':100, 'fuel_cost':2.4},
                engine_types[1]:{'race':150000, 'fuel_rate':6, 'dif_price':120, 'fuel_cost':1.8}
               }
# print(engine_types[1])
# print(engine_info['Diesel']['fuel'])
def gen_race():
     return random.randint(29000, 186000)

class Car(object):
     __count = 0
     def __init__(self, price=10000):
         self.__class__.__count+=1

         self.__number = self.__count

         self.__price = price

         if self.__count%3 == 0:
             self.__engine_type = engine_types[1]
         else: self.__engine_type = engine_types[0]

         self.__max_race = engine_info[self.__engine_type]['race']
         self.__fuel_rate = engine_info[self.__engine_type]['fuel_rate']
         self.__dif_price = engine_info[self.__engine_type]['dif_price']
         self.__fuel_cost = engine_info[self.__engine_type]['fuel_cost']

         if self.__count%5 == 0:
             self.__tank = 75
         else: self.__tank = 60

         self.__race =  0 # self.set_race(0)
         self.__value = price
         self.__used_fuel = 0
         self.__remain_race = 0
         self.__costs = 0

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
     value = property(get_value, set_value)

     def set_used_fuel(self):
         self.__used_fuel = int(self.__race) * int(self.__fuel_rate) / 100
     def get_used_fuel(self):
         return self.__used_fuel
     used_fuel = property(get_used_fuel, set_used_fuel)

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
    a = []
    for i in range(30):
        a.append(Car())
        a[i].race = gen_race()
        print('race='+str(a[i].race)+'km')
        # print(a[i].__dict__)
        print('value=' + str(a[i].value)+'$')
        print('used_fuel='+str(a[i].used_fuel)+'L')
        print('remain race='+str(a[i].remain_race)+'km')
        print('#####################################')
    b = sorted(a)
    for i in b:
        print(i.get_number(), i.get_type(), i.remain_race, i.value)

