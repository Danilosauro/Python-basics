from turtle import clearscreen, delay


a = int(input ('Digite o primeiro valor: '))
b = int(input ('Digite o segundo  valor:' ))
c = int(input ('Digie  o terceiro valor:' ))

if a > b and a > c : 
    print("o número", a , "é o maior")

elif b > a and b > c:  
    print("o numero", b , "é o maior")  

elif c > a and c > b: 
    print("O número", c, "é o maior") 

else: 
    print("Os números são iguais")

# parte dois, numero par 

d = int(input('Digite um novo valor:  ')) 
e = int(input('Digite mais um valor:  '))

restod =d % 2
restoe =e % 2 

if restod==0 and restoe ==0: 
    print("Os numeros", d ,"e ", e, "sao pares.")

if restod==0 and restoe !=0:
    print("O numero", d , "e", "par, e o numero", e , "e impar") 

if restod !=0 and restoe ==0: 
    print("o numero", d , "e impar, e o numero", e , "e par ")

elif restod !=0 and restoe !=0:
    print("os numeros", d , "e", e, "sao impares")
