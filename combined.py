# Creating 2 lists containing integers
# The last list is the result of the 2 first combined

numbers1 = [12, 3, 5, 1, 56, 109]
numbers2 = [25, 10, 2, 45, 7, 13, 99]
all_numbers = numbers1 + numbers2

# Creating the text file numbers1 and sorting from smallest to largest
# Using the for loop and write to the file

with open('numbers1.txt', 'w') as f:
    numbers1.sort()
    for line in numbers1:
        f.write(str(line) + "\n")

 # Creating the text file numbers2 and sorting from smallest to largest
 # Using the for loop and write to the file

with open('numbers2.txt', 'w') as f:
    numbers2.sort()
    for line in numbers2:
        f.write(str(line) + ("\n"))

# Creating the text file all_numbers
# Sorting the combined numbers from smallest to largest using the sort() function
# Using the for loop to write to the file

with open('all_numbers', 'w') as f:
    all_numbers.sort()
    for number in all_numbers:
        f.write(str(number) + ("\n"))
