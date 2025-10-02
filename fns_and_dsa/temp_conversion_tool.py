# temp_conversion_tool.py
# Script to demonstrate variable scope with global conversion factors

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Conversion functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main program
if __name__ == "__main__":
    try:
        # Ask user for temperature
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)  # Validate numeric

        # Ask for the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
        elif unit == "C":
            print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
        else:
            # Wrong unit → raise error
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
    
    except ValueError as e:
        # Raise error exactly as required
        raise ValueError("Invalid temperature. Please enter a numeric value.")
