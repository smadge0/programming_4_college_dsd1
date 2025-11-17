def tempconverter(unit, temp):
    if unit == "celsius" or unit == "C" or unit == "Celsius":
        temp = (temp * 9/5) + 32
    elif unit == "fahrenheit" or unit == "F" or unit == "Fahrenheit":
        temp = (temp - 32) * 5/9

    return str(temp)

unit = input("How do you measure temperature? (Celsius or Fahrenheit) ")
temp = int(input("Enter a temperature to convert it to the other unit! "))

if unit == "fahrenheit" or unit == "F" or unit == "Fahrenheit":
    temp = (temp - 32) * 5/9
    print(f"Your fahrenheit temperature is equivalent to", {temp}, "celsius!")
elif unit == "celsius" or unit == "C" or unit == "Celsius":
    temp = (temp * 9/5) + 32
    print(f"Your celsius temperature is equivalent to", {temp}, "fahrenheit!")
