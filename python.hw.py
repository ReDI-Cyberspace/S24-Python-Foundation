## task 1
num1 = int(input("type a number: "))
print(num1)
num2 = int(input("type another number: "))
print(num2)
# each variable must have a modulo equal to zero to qualify as an even number
if num1 % 2 == 0 and num2 % 2 == 0:
    print(True)
else:
    print(False)
# each variable must have a modulo equal to zero to qualify as an odd number
if num1 % 5 == 0 or num2 % 5 == 0:
    print("multiply by 5 is possible in one of the numbers")
## PS C:\Users\rahel\OneDrive\Desktop\python.hw> & C:/Users/rahel/AppData/Local/Programs/Python/Python312/python.exe c:/Users/rahel/OneDrive/Desktop/python.hw/python.hw.py
# type a number: 15
# 15
# type another number: 14
# 14
# False
# multiply by 5 is possible in one of the numbers
# PS C:\Users\rahel\OneDrive\Desktop\python.hw>

## task 2
weather_today = float(input("type the weather today in Celcius: "))
print(weather_today)
if weather_today < 12:
    print("wear a jacket")
if weather_today < 4:
    print("wear a pair of gloves")
if weather_today < 8:
    print("wear a scarf")
if weather_today > 25:
    print("wear sunglasses")
# the inputted weather is printed as a float and qualifies for three of the conditions
## type the weather today in Celcius: 3
# 3.0
# wear a jacket
# wear a pair of gloves
# wear a scarf

## task 3
steak = 3
# the variable for the first friend is defined to then see which if conditions below will be met
if steak < 2:
    print("the steak is rare")
if steak > 2 and steak < 4:
# this condition is between two numbers    
    print("the steak is medium")
if steak > 4:
    print("the steak is well-done")
if steak > 8:
    print("the steak is burnt")
print("The steak is perfect for friend 1!")
# unindented print function stops the code
# the printed answers: 
# the steak is medium
# The steak is perfect for friend 1!

steak = 10
# the variable for the second friend is defined to then see which if conditions below will be met
if steak < 2:
    print("the steak is rare")
if steak > 2 and steak < 4:
# this condition is between two numbers
    print("the steak is medium")
if steak == 4:
    print("the steak is well-done")
if steak > 8:
    print("the steak is burnt")
print("You ruined the steak!Friend 2 is furious")
# unindented print function stops the code
# the printed answers:
# the steak is burnt
# You ruined the steak! Friend 2 is furious





