class Programmer:
    company = "Microsoft"

    def __init__(self,name,language):
        self.name = name
        self.language = language
        

employee1  = Programmer("Hamza Abbas" , "Python")        
employee2= Programmer("Ali" , "Java")        


print(employee1.name, employee1.language,employee1.company)
print(employee2.name, employee2.language,employee2.company)

