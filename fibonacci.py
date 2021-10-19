def febFunction(n):
    a = 0
    b = 1
    if n == 0:
        return 0
    elif n == 1 :
        return 1
    else:
        print(a)
        print(b)
        for i in range (2 , n):  
            c = a + b
            a = b
            b = c
            print(c)
        print("gulden snede is : ")
        return c
k = 5             
print(febFunction(10) , febFunction(k))
