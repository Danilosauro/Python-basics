from heapq import merge


conjunto1 = {1,2,3,4,5,6,7} 
conjunto2={5,6,7,8}

conjunto1.add(5) # adiciona
conjunto1.discard(5) # remove
 

conjunto_uniao = conjunto1.union(conjunto2)
print(conjunto_uniao)
conjunto_interseccao = conjunto1.intersection(conjunto2)  
print(conjunto_interseccao)
conjunto_diferenca = conjunto1.difference(conjunto2)
print(conjunto_diferenca)
 


