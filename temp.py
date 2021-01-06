# -*- coding: utf-8 -*-



"""3) Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num.
HINT 1: Use the accumulation pattern!
HINT 2: the in operator checks whether a substring is present in a string."""

items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0
for i in items:
    if "w" in i:
        acc_num += 1
print(acc_num)
4







"""1) The variable sentence stores a string. Write code to determine how many words in sentence start and end with the same letter, including one-letter words. Store the result in the variable same_letter_count.
."""

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
sentence = sentence.split(" ")
#print(sentence)
same_letter_count = 0

for j in sentence:
     if j[:1]==j[-1:]:

        same_letter_count +=1
print (same_letter_count)



"""2) rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every month separated by a comma. Write code to compute the number of months that have more than 3 inches of rainfall. Store the result in the variable num_rainy_months. In other words, count the number of items with values > 3.0."""


rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
rainfall_mi = rainfall_mi.split(",")
num_rainy_months = 0
for i in rainfall_mi:
    if float(i) > 3.0:
        num_rainy_months +=1
print (num_rainy_months)


"""3) Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num.
HINT 1: Use the accumulation pattern!
HINT 2: the in operator checks whether a substring is present in a string."""

items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0
for i in items:
    if "w" in i:
        acc_num += 1
print(acc_num)