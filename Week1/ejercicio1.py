cant_datos = int(input())
lista_numero = [int(x) for x in input().split()]

def max_prod(n):
    n.sort()
    max_v = n[-1]
    sec_max_v = n[-2]
    answ = max_v * sec_max_v
    return answ 


print(max_prod(lista_numero))
