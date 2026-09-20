def table(n , i = 1):
    if i > 10:
        return
    print(f"{n} X {i} = {n * i}"  )
    table(n , i + 1)
result = int(input("Enter a number: "))    
table(result)
   