# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]
print(len(fruits))

# Challenge:
# Use a for loop to print each fruit on a new line.
print(fruits[0])
print(fruits[1])
print(fruits[2])
for fruit in fruits:
    print(fruit)
# i just worked with loops

# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
for subject in subjects:    
    print(subject)

# print out each subject but stop when you reach "History"
for subject in subjects:
    if subject == "History":
        break
    print(subject)
# skip over "Science" and print the rest
for subject in subjects:
    if subject == "Science":
        continue
    print(subject)

list1000 = list(range(1, 1001))
# break when you reach a number greater than 599
for number in list1000:
    if number > 599:
        break
    print(number)

# skip over 300-500 and print the rest
for number in list1000:
    if 300 <= number <= 500:
        continue
    print(number)

# Another way to skip over numbers
for number in list1000:
    if number >= 300 and number <= 500:
        continue
    print(number)


applicants_for_credit = ["Alice", "Bob", "Charlie", "David", "Eve"]
credit_scores = [720, 680, 590, 610, 750]
# zip the two lists together and print
# each applicant's name along with their credit score.
# if the score is below 600, skip over that applicant.
# and approve the rest for credit.


for applicant, score in zip(applicants_for_credit, credit_scores):
    # zip function combines two lists into pairs
    if score < 600:
        continue
    print(applicant + " approved for credit with score: " + str(score))



# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"


# Given:
numbers = [5, 10, 15, 20]

# Challenge:
# Use a for loop to add all the numbers and print the total.