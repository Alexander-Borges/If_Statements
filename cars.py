cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car =="bmw":
        print(car.upper())
    else:
        print(car.title())

# Conditional Tests
# Checking for Equality
car1 = 'bmw'
car1 =='bmw'

car2 = 'audi'
car2 =='bmw'

# If case does not matter when you want to test the value of your variable, you can convert the variable's value to lowercase before doing the comparison:
car = "Audi"
car.lower()=="audi"
# at line 17 we assign the capitalized string "Audi" to the variable car. At line 18 we convert the value of car to lowercase and compare the lowercase value to the string 'audi'. the two strings match, so Python returns True. 