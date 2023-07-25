name = input("What is your name? ")         #Stores the value from input() in the variable name
print(name)

name = "Somu"
print(name)         #Replaces the value of name

name = input("What is your name? ")
length = str(len(name))
print("Length of your name is " + length)

#program that switches the values stored in the variables a and b
a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)