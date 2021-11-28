# hallar el GCD  de dos numeros

n1 = int(input("n1: "))
n2 = int(input("n2: "))

def GCD_No_Efficient(a,b):
    mark = 0
    if a > b:
        mark = b
    else:
        mark = a
    for i in range(0,mark):
        if((a%i==0) and (b%i==0)):
            value = i
    return value

print(GCD_No_Efficient(n1,n2))