import math
import calculator

# import math, calculator # allowed but not recommended

print(math.__name__) # __name__ is dunder method
print(calculator.__name__)
print(__name__) # if the file is the place which runs the program (launching point) dunder name of the file will be __main__

print(calculator.area(5))

