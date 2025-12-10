# Given:
colors = ["red", "blue", "green", "yellow", "purple"]
print(len(colors)) # output: 5
# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".
# Do NOT print "yellow" — stop before it.
index = 0
while index < len(colors):
    # colors = ["red", "blue", "green", "yellow", "purple"]
    if colors[index] == "yellow":
        break
    print(colors[index])
    index += 1
    # index += 1 is shorthand for index = index + 1
# Explanation:
# We start with index 0 (first color)
# while index is less than legth of colors (5)
# Check if color at current index is "yellow"