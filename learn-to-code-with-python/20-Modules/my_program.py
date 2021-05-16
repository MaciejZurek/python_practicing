import calculator # python imports module only once, so if this line will repeat, nothing will happen

print("^ This is coming from calculator.py")

print(calculator.creator) # calculator.X is necessary, because creator and PI are in the calculator's namespace, not in my_program
print(calculator.PI)
print(calculator.add(3,5))
print(calculator.subtract(1,100))