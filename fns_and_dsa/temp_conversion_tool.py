# temp_conversion_tool.py
# Demonstrates variable scope with global conversion factors

# 1. Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# 2. Conversion functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# 3. User interaction
if __name__ == "__main__":
    temp_input = input("Enter the temperature to convert: ")
    try:
        # Validate numeric input
        temperature = float(temp_input)
    except ValueError:
        # 4. Raise ValueError if input is not numeric
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
    elif unit == "C":
        print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
    else:
        # 5. Raise ValueError if unit is invalid
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
