def natural_sum(n):
    if n == 1:
       return 1
    else:
        return n + natural_sum(n - 1)
number = int(input("Enter a number: "))
result = natural_sum( number )
print(result)    