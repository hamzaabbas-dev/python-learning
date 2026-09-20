def star_pattern(n):
    for i in range (n , 0 , -1):
        for j in range(i):
            print("*",end="")
          
        print()     
           
star_pattern(int(input("Enter a number: ")))
