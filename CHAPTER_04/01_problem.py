# Write a program to create a dictionary of Urdu words as their English translation .Provide user with an option to look it up !

dictionary ={
    "koshish krna" : "Efforts" ,
    "sona" : "Sleep",
    "khana" : "Eating",
    "madad krna" : "Help"
}

word = input("Enter the word you want meaning of:")
word1 = word.strip().lower()
print(dictionary.get( word1 , "Not Found"))