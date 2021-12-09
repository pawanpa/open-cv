#Python program to print even length words in a string.
a = input("enter the string: ")
b=[]
for i in range((len(a)-1)):
    if i%2 != 0:
        b.append(a[i])
        c="".join(b)
        print(c)


