class Calculator:
    #Class Attribute
    calculation_type = "Arithmetic Operations"

    #Static method does not use self or cls
    @staticmethod
    def add(a, b):
        return a + b
    
    # Class method - accesses class-level data via cls
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b 
