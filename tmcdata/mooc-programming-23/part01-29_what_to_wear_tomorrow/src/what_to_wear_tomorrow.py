# Write your solution here

# Please write a program which asks for tomorrow's weather forecast and then suggests weather-appropriate clothing.

# The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also if there is rain on the radar.

# Some examples of expected behaviour:

# Sample output
# What is the weather forecast for tomorrow?
# Temperature: 21
# Will it rain (yes/no): no
# Wear jeans and a T-shirt
# Sample output
# What is the weather forecast for tomorrow?
# Temperature: 11
# Will it rain (yes/no): no
# Wear jeans and a T-shirt
# I recommend a jumper as well

print("What is the weather forecast for tomorrow?")
temp = int(input("Temperature: "))
rain_tomorrow = input("Will it rain (yes/no) ")

if temp > 0:
    print("Wear jeans and a T-shirt")
if temp <= 20:
    print("I recommend a jumper as well")
if temp <= 10:
    print("Take a jacket with you")
if temp <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if rain_tomorrow == 'yes':
    print("Don't forget your umbrella!")