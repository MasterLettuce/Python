def nume_par(num):
    divi=num%2
    if divi==0:
        return("es par")
    else:
        return("no es par")

def primos(num):
    divi=[]
    for i in range(1,num+1):
        divi.append(num%i)
    eva=divi.count(0)
    if eva==2: 
        return("es primo")
    else:
        return("no es primo")

def fibonacci(num):
    f1=0
    f2=1 
    fibo=[]
    for i in range(1,20):
        fibo.append(f1)
        sig=f1+f2
        f1=f2
        f2=sig  
        i += 1
    eva=fibo.count(num)
    if eva==0:
        return("no es fibonacci")
    else:
        return("es fibonacci")


print("ingresa el valor que deseas evaluar")
num=int(input())
print("El numero",num,":")
print(nume_par(num),",",primos(num),",",fibonacci(num))
