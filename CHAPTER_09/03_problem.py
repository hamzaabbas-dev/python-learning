class Demo:
     a = 10

test1 = Demo()
test2 = Demo()

test1.a = 0

print(test1.a)
print(test2.a)
print(Demo.a)