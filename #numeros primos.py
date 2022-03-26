#numeros primos 

a=  int(input("entre com o número:"))  

if a ==2 or a ==3: 
    print("o número é primo") 


restoa = a  % 2 
restoadois = a % 3

if  a !=2 and a !=3: 
    if restoa==0 or restoadois == 0:
        print("o número não é primo")


if a !=1 and a !=2 and a !=3: 
    if restoa !=0 and  restoadois !=0: 
        print(" o número é primo")