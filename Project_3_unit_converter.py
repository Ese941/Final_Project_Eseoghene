print("Welcome to the unit converter app \n")
user = input("Which of these operations would you like to carry out: \n 1. Kilometers to Miles \n 2. Kilograms to Pounds \n 3. Celsuis to Fahrenheit \n")
if user == "1":
    def kilometers_to_miles(kilometers):
        miles = (kilometers * 0.62137)
        return miles
    user =  float(input("Enter your value in kilometers: "))
    print(f"The value in Miles is {kilometers_to_miles(user)}")

elif user == "2":
    def kilograms_to_pounds(kilograms):
        pounds = (kilograms * 2.20462)
        return pounds
    user = float(input("Enter your value in kilogram: "))
    print(f"The value in pounds is {kilograms_to_pounds(user)}")

elif user == "3":
    def celsuis_to_fahrenheit(celsuis):
        fahrenheit = (celsuis *9/5) + 32
        return fahrenheit
    user = float(input("Enter your temperature in celsuis: "))
    print(f"The temperature in fahrenheit is {celsuis_to_fahrenheit(user)} ")

else:
    print("We do not perform such an operation!")
