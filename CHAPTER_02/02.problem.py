# Write a program to fil in a template given below with name and date

letter = ''' DEAR <|name|>,
You are selected !
 <|date|>
 '''
print(letter.replace("<|name|>","Hamza Abbas").replace("<|date|>", "31 july 2026"))