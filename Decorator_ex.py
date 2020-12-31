

def car_category(function):
    def inner(name,speed,year):
        function(name,speed,year)
        if speed > 100:
            print("It's Sport Car !!!")
        else:
            print("It's Normal Car !!!")
    return inner

def new_or_old(function):
    def one_more(name,speed,year):
        function(name,speed,year)
        if year > 10:
            print("It'S Very Old Car")
        else:
            print("It's New Car")
    return one_more

@new_or_old
@car_category
def car(name,speed,year):
    print(f"My Car Name Is {name} And It's Speend Is {speed}km/h,It's {year} Year Old Car")

# obj = car_category(car)
# obj("i10",99,2)

car('BMW',200,5)