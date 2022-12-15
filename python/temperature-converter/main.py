def convert_temp(temp, unit):
    if unit == "f":
        return (temp - 32) * 5/9
    elif unit == "c":
        return temp * 9/5 + 32
    else:
        return "Error: Unit not recognized"

#Get the user's input
temp = float(input("Enter a temperature: "))

unit = input("Enter the unit of the temperature (f, c): ")
# retry if the unit is not f or c
while unit != "f" and unit != "c":
    print("Error: Unit not recognized, please type f or c")
    unit = input("Enter the unit of the temperature (f, c): ")

#Convert the temperature
converted_temp = convert_temp(temp, unit)

#Print the converted temperature

if unit == "f":
    typeunit = "celsius"
elif unit == "c":
    typeunit = "fahrenheit"

print("The converted temperature is " + str(converted_temp) + " degrees " + typeunit + ".")

