#metohd cahing calling each method sequnetialy
class Car:
    def drive(self):
        print("the car is drving")
        return self

    def  stop(self):
        print('the has stopped')
        return self

    def brakes(self):
        print("you step on the brakes")
        return self

    def engine(self):
        print('strat the engine')
        return self

car=Car()
car.stop()\
    .drive()\
    .engine()\
    .brakes()