n1 = int(input())
n2 = int(input())

def GDC_Tuneado(a,b):
  if b>a:
    if b % a == 0:
      return a
    else:
      return GDC_Tuneado(b%a,a)
  else:
    if a % b == 0:
      return b
    else:
      return GDC_Tuneado(b,a%b)

print(GDC_Tuneado(n1,n2))