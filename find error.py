a = int(input("Enter number 'a': "))
b = int(input("Enter number 'b': "))
c = int(input("Enter number 'c': "))

if a == b == c:
    print("The values are equal")

elif (a > b) and (a > c):
    print("a is greatest and the value is {}".format(a))

elif (b > a) and (b > c):
    print("b is greatest and the value is {}".format(b))

else:
    print("c is greatest and the value is {}".format(c))

print()

