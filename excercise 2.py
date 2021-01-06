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
