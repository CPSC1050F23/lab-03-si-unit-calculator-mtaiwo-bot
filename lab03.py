"""
Welcome to Lab 03.

Author: Folu Taiwo
Date:9/12/23
Assignment: Lab 03
Course: CPSC 1051
Lab Secion: 003

Code Description: Creating a caculator using the SI Unit system to calculate units like 
distance, temperature, and mass. To do that we will utilize branches and booleans so we 
can convert our American Imperial units to the metric system.


We will be grading for Header, Comments, Formatting.

Follow the instructions in the lab document. 
Write your code to complete the tests in the Gradescope autograder.

"""
"Necessary statements:"
if meters == cm:
    meters = cm/100
elif meters == km:
    meters = km*1000
elif meters == inches:
    meters = inches*0.0254
elif meters == ft:
    meters = ft*0.3048

 
"""
"Please select one of the following to convert to meters: cm m km in ft: "
"Please select one of the following to convert to grams: mg g kg lbs: "
"Please select one of the following to convert to meters per second: m/s km/h ft/s mph: "
"Please select one of the following to convert to Celcius: C F K: "

"Please input a value: "
"Unsupported unit"
"Invalid unit type"

"""

print("Welcome to the convert to SI units calculator!")
print("Please input a type of unit that you would like \nto convert. Here are your options: \ndistance \nmass \nspeed \ntemperature\n")
#Ask user for input on what measurement
measurement = str(input()).strip()
if measurement == "distance":
    print("Please select one of the following to convert to \nmeters: cm m km in ft: ")
elif measurement == "mass":
    print("Please select one of the following to convert to \ngrams: mg g kg lbs: ")
    if value < 0:
        print("You can't have a negative mass!")
elif measurement == "speed":
    print("Please select one of the following to convert to \nmeters per second: m/s km/h ft/s mph: ")
elif measurement == "temperature":
    print("Please select one of the following to convert to \nCelcius: C F K: ")
elif measurement != ["distance", "mass", "speed", "temperature"]:
    print("Invalid unit type")
else:
    print("Unsupported unit")
choice = str(input()).strip()
print("Please input a value: ")
value = int(input())
print(f"{value:.2f} {choice} in : ")


