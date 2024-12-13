#range goes to the number before the last number in the range

def fizz_buzz(self):
    if self % 3 == 0 and self % 5 == 0:
        return "FizzBuzz"
    elif self % 3 == 0:
        return "Fizz"
    elif self % 5 == 0:
        return "Buzz"
    else: return str(self)
