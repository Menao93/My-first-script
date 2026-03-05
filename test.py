

name = input("Hey, What is your name? ")
print("Hello, " + name)

age = int(input("How old are you, " + name + "? "))
if age >= 18:
 print("You are an adult.")
else:print("You are a minor.")

print("You must have been born in " + str(2026 - age))
print("goodbye " + name + ", It was nice talking to you")