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
print("Please input a type of unit that you would like to convert. Here are your options: \ndistance \nmass \nspeed \ntemperature\n")
#Ask user for input on what measurement
measurement = str(input()).strip()
#Ask user to select unit type to convert based on measurement user inputted
if measurement == 'distance':
    print("Please select one of the following to convert to meters: cm m km in ft: ")
#If user inputs a type of unit that can not be converted the program will print 
#Invalid unit type
elif measurement != 'distance':   
    print("Invalid unit type")
elif measurement == 'mass':
    print("Please select one of the following to convert to grams: mg g kg lbs: ")
elif measurement != 'mass':
    print("Invalid unit type")
elif measurement == 'speed':
    print("Please select one of the following to convert to meters per second: m/s km/h ft/s mph: ")
elif measurement != 'speed':
    print("Invalid unit type")
elif measurement == 'temperature':
    print("Please select one of the following to convert to Celcius: C F K: ")
elif measurement != 'temperature':
    print("Invalid unit type")

   
#Ask user for unit they want to convert
u_unit = str(input()).strip()
#Ask user for value they want to convert
u_val = float(input("Please input a value: \n"))

#This is a nessested if-else statement. This is used to determnine the unit the user selected and convert it
#into meters. The first branch is if the user imports a negative value because it will print You 
#can't have a negative distance
if u_val < 0:
    print("You can't have a negative distance!")     
elif u_unit == 'cm':
    con = u_val / 100
    print(f'{u_val:.2f} {u_unit} in meters: {con:.2f}')
elif u_unit != 'cm':
    print("Unsupported unit")
    print("Please select one of the following to convert to meters: cm m km in ft: ")
elif u_unit == 'm':
    con = u_val
    #Since meters does not need to be converted the new value is the same as the one inputted
    print(f'{u_val:.2f} {u_unit} in meters: {con:.2f}')
elif u_unit != 'm':
    print("Unsupported unit")
    print("Please select one of the following to convert to meters: cm m km in ft: ")
elif u_unit == 'km':
    con = u_val * 1000
    print(f'{u_val:.2f} {u_unit} in meters: {con:.2f}')
elif u_unit != 'km':
    print("Unsupported unit")
    print("Please select one of the following to convert to meters: cm m km in ft: ")
elif u_unit == 'in':
    con = u_val * 0.0254
    print(f'{u_val:.2f} {u_unit} in meters: {con:.2f}')
elif u_unit != 'in':
    print("Unsupported unit")
    print("Please select one of the following to convert to meters: cm m km in ft: ")
elif u_unit == 'ft':
    con = u_val * 0.3048
    print(f'{u_val:.2f} {u_unit} in meters: {con:.2f}') 
elif u_unit != 'ft':
    print("Unsupported unit")
    print("Please select one of the following to convert to meters: cm m km in ft: ")

if u_val < 0:  
    print("You can't have a negative mass!")
elif u_unit == 'mg':
    con = u_val / 1000
    print(f'{u_val:.2f} {u_unit} in grams: {con:.2f}')
elif u_unit != 'mg':
    print("Unsupported unit")
    print("Please select one of the following to convert to grams: mg g kg lbs: ")
elif u_unit == 'g':
    con = u_val
    print(f'{u_val:.2f} {u_unit} in grams: {con:.2f}')
elif u_unit != 'g':
    print("Unsupported unit")
    print("Please select one of the following to convert to grams: mg g kg lbs: ")
elif u_unit == 'kg':
    con = u_val * 1000
    print(f'{u_val:.2f} {u_unit} in grams: {con:.2f}')
elif u_unit != 'kg':
    print("Unsupported unit")
    print("Please select one of the following to convert to grams: mg g kg lbs: ")
elif u_unit == 'lbs':
    con = u_val * 453.592
    print(f'{u_val:.2f} {u_unit} in grams: {con:.2f}')
elif u_unit != 'lbs':
    print("Unsupported unit")
    print("Please select one of the following to convert to grams: mg g kg lbs: ")
 
if u_val < 0:
    print("You can't have a negative speed!")
elif u_unit == 'm/s':
    con = u_val
    print(f'{u_val:.2f} {u_unit} in grams: {con:.2f}')
elif u_unit != 'm/s':
    print("Unsupported unit")
    print("Please select one of the following to convert to meters per second: m/s km/h ft/s mph: ")
elif u_unit == 'km/h':
    con = u_val * 0.277778
    print(f'{u_val:.2f} {u_unit} in meters per second: {con:.2f}')
elif u_unit != 'km/h':
    print("Unsupported unit")
    print("Please select one of the following to convert to meters per second: m/s km/h ft/s mph: ")
elif u_unit == 'ft/s':
    con = u_val * 0.3048
    print(f'{u_val:.2f} {u_unit} in meters per second: {con:.2f}')
elif u_unit != 'ft/s':
    print("Unsupported unit")
    print("Please select one of the following to convert to meters per second: m/s km/h ft/s mph: ")
elif u_unit == 'mph':
    con = u_val * 0.44704
    print(f'{u_val:.2f} {u_unit} in meters per second: {con:.2f}')
elif u_unit != 'mph':
    print("Unsupported unit")
    print("Please select one of the following to convert to meters per second: m/s km/h ft/s mph: ")

if u_val < 0:
    print("You can't have a negative temperature!")
elif u_unit == 'C':
    con = u_val
    print(f'{u_val:.2f} {u_unit} in celcius: {con:.2f}')
elif u_unit != 'C':
    print("Unsupported unit")
    print("Please select one of the following to convert to Celcius: C F K: ")
elif u_unit == 'F':
    con = (u_val - 32) * (5/9)
    print(f'{u_val:.2f} {u_unit} in celcius: {con:.2f}')
elif u_unit != 'F':
    print("Unsupported unit")
    print("Please select one of the following to convert to Celcius: C F K: ")
elif u_unit == 'K':
    con = u_val - 273.15
    print(f'{u_val:.2f} {u_unit} in celcius: {con:.2f}')
elif u_unit != 'K':
    print("Unsupported unit")
    print("Please select one of the following to convert to Celcius: C F K: ")






