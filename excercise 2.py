# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 18:24:46 2021

@author: Nermeen.Moustafa
"""

"""Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro. Only the first letter of each word should be used, each letter in the acronym should be a capital letter, and there should be nothing to separate the letters of the acronym. Words that should not be included in the acronym are stored in the list stopwords. For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”."""

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro = ""

org = org.split(" ")
for i in org:
    if i not in stopwords:
        acro += i[0:1].upper()
        
print(acro)            


"""We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words."""

emotions = open("emotion_words.txt", "r")
contents = emotions.readlines()
num_words = 0
for lin in contents:
    words = lin.split(" ")
    total_words = len(words)
    num_words += total_words
    

   
print(num_words)

""" We have a file named school_prompt of lines of words and we want to create a list named three that contains words composed of up to 3 letters"""

schoolprompt = open("school_prompt.txt", "r")
contents = schoolprompt.readlines()
#print(contents)
three = []
for word in contents:
    words=word.split(" ")
    #print(words)
    for wrd in words:
        if wrd== wrd[:3]:
            three.append(wrd)
    
print(three)

