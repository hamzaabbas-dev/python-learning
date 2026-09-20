def greatest(a,b,c):

    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c

greatest_no = greatest(10, 5, 24)
print("The Greatest no is : " , greatest_no)    