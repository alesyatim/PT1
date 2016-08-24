import random
engine_types = ['Petrol', 'Diesel']
engine_info = {
                engine_types[0]:{'race':20000, 'fuel':8, 'dif_price':100},
                engine_types[1]:{'race':10000, 'fuel':6, 'dif_price':120}
               }

print(engine_types[1])
print(engine_info['Diesel']['fuel'])

def gen_race():
    return random.randint(29000, 186000)

class Car(object):
    __count = 0
    def __init__(self, price=10000):
        self.__class__.__count+=1

        self.__price = price


        if self.__count%3 == 0:
            self.__engine_type = engine_types[1]
        else: self.__engine_type = engine_types[0]

        self.__max_race = engine_info[self.__engine_type]['race']
        self.__fuel = engine_info[self.__engine_type]['fuel']
        self.__dif_price = engine_info[self.__engine_type]['dif_price']

        if self.__count%5 == 0:
            self.__tank = 75
        else: self.__tank = 60

        self.race =  0
        self.__value = price
        self.__used_fuel = 0
        self.__remain_race = 0

        def get_race(self):
            return self.__race

        def set_race(self, race):
            self._race = race
            print('in', self._race)
            if self._race > self.__max_race:
                self._race = self.__max_race
            self.set_value()
        race = property(get_race, set_race)

        def set_value(self):
            self.__value =  int(self.__price) - int(self.__race) * int(self.__dif_price)/ 1000
            if self.__value < 0:
                self.__value = 0
        def get_value(self):
            return self.__value
        value = property(get_value, set_value)





a = []
for i in range(30):
   a.append(Car())
   print('race='+str(a[i].race))
   print(a[i].__dict__)
   #print('value=' + str(a.value))