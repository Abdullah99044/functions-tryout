def multiplierFunction(x: int):
    for n in range(1,11):
        resultaat = n * x
        print(n , " x " , x , (" = ") , resultaat )

answer = int(input("Van welk getal wilt u de tafel zien? : "))

multiplierFunction(answer)