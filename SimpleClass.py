#car , type , model , price ,  milesDrive, owner


class Car:



    #creating our contructor
    def __init__(self,carType,carModel,carPrice,milesDriven,carOwner):
        self._CarType = carType
        self._CarModel = carModel
        self._CarPrice = carPrice
        self._MilesDriven = milesDriven
        self._CarOwner = carOwner
    def GetType(self):
        return self._CarType

    def GetCarModel(self):
        return self._CarModel

    def GetCarPrice(self):
        return self._CarPrice

    def GetMilesDriven(self):

        return self._MilesDriven

    #getter and setter for car owner

    def GetCarOwner(self):
        return self._CarOwner

    def GetPrice(self):
        return self.GetCarPrice() - (self.GetMilesDriven()*10)


def main():

    print("this is main : ")

    #carType
    myCar = Car("bmwife",2015,25000,15,"wandie")
    currentPriceCar = myCar.GetPrice()
    print("New Price is : {}".format(currentPriceCar))





if __name__ == '__main__':main()