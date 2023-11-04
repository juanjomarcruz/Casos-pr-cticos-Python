def es_primo(x):
  if x<=1:
    return False
  for i in range(2,x):
      if x%i==0:
        return False
  return True
def n_primos(n):
  lista_primos=[]
  contador=0
  i=0
  while contador<n:
    if es_primo(i)==True:
      lista_primos.append(i)
      contador+=1
    i+=1
  print(lista_primos)
  return lista_primos
n_primos(9)