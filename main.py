import random
class Human:
    def __int__(self, name = "Кучма Марія Денисівна", job = None, home = None, car = None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 1000
        self.gladness = 50
        self.satiety = 50
    def get_home(self):
        pass
    def get_job(self):
        pass
    def get_car(self):
        pass
    def food(self):
        pass
    def work(self):
        pass
    def shopping(self):
        pass
    def chill(self):
        pass
    def clean_home(self):
        pass

    def day_indexes(self):
        pass
    def is_alive(self):
        pass
    def live(self):
        pass

class Auto:
    def __int__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.strength = brand_list[self.brand]["strength"]
        self.fuel = brand_list
























