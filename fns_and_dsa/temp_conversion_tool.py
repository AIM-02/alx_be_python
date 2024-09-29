#global variables
fahrenheit_to_celsius_factor = 5 / 9
celsius_to_fahrenheit_factor = 9 / 5

#convert fahrenheit to celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * fahrenheit_to_celsius_factor
    return celsius

#convert celsius to fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * celsius_to_fahrenheit_factor) + 32
    return fahrenheit
def main():
    temperature = float(input("enter the temperature to convert: "))
    unit_of_measurement = input("is the temperature in celsius or in fahrenheit? (C/f): ")
    if unit_of_measurement == 'fahrenheit':
        converted_temperature = convert_to_celsius(temperature)
        print(f"{temperature}F is {converted_temperature}C")
    elif unit_of_measurement == 'celsius':
        converted_temperature = convert_to_fahrenheit(temperature)
        print(f"{temperature}C is {converted_temperature}F")
    else:
        print("invalid temperature, please enter a numeric value")
    
if __name__ == "__main__":
        main()    