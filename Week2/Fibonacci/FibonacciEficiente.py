

def FibList(n):
    """
    1 - create an array to store all the numbers
    2 - first element 0 and second element 1
    3 - iterate throught the list 
    4 - from i from 2 to 1
    5 - add the 
    
    """
    num = [0,1]
    for i in range(2,n+1):
        num.append(num[-1] + num[-2])
    return num
print(FibList(5))