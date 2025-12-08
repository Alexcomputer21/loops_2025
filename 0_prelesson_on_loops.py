# Loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
# While loops  

# for loops = execute a block of code a fixed nmuber of times.
#     You can iterate over a range, string, sequence, etc.


# practice don't use for refernce I did it wrong:

credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)
print("HAPPY NEW YEAR!")


for x in range(1,21):
    if x == 13:
        break
    else:
        print(x)

# while loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")


while name == "":
    print("You did not enter your name")
print(f"Hello {name}")


while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))
print(f"You are {age} years old")