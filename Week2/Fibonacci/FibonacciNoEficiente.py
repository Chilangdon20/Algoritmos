n = 4

def Fibrec(num):
    if num <= 1:
        return num
    else: 
        # T(n) = 3 code lines + T(n-1) + T(n-2)
        # in this case the output is 3 because the
        # 4rd elemnt  of the sequence is 3
        # 0  1 1 2 3
        return Fibrec(num-1) + Fibrec(num-2)

print(Fibrec(n))