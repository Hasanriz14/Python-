from random import randint

class Get_data:
    def __init__(self):
        print('hello')
        self.dt = []
        self.get_x = []
        self.get_y = []
    def send_data(self):
        while len(self.dt) < 20:
            self.dt.append(randint(1,20))
            original_list = list(set(self.dt))
            original_list.reverse()
        return original_list
    def scatter_data_x(self):
        while len(self.get_x) < 6:
            self.get_x.append(randint(1,50))
        return self.get_x
    def scatter_data_y(self):
        while len(self.get_y) < 6:
            self.get_y.append(randint(1,50))
        return self.get_y            
