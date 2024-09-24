class Fraction:
    numerator=0
    denominator=1

    def __init__(self, num, den):
        self.numerator = num
        self.denominator = den
    
    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"