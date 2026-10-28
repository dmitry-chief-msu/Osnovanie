class Car:
    def ride(self):
      print('Едет по дороге')

class Boat:
    def swim(self):
      print('Ходит по воде')

    def play(self):
        print ('Играет Чайковского')

class Amphibian(Car, Boat):
    def display(self):
        print ('Амфибия:')


 #   def ride(self):