#conversor de temperaturas

def CaF(x):
    # de celcius a farenheit
    FH=x*(9/5)+32
    return FH

def CaK(x):
    # de celcius a kelvin
    Kvn=x+273.15
    return Kvn
    
def CaR(x):
    # de celcius a Rankine
    Rkn=x*(9/5)+491.67
    return Rkn
print(" Escalas de temperatura Celcius(c),Farenheit(f), Kelvin(k), Rankine(r)")
print("Indica la escala que tienes:")
inicial=input()
print("Indica la escala que deseas:")
final=input()

if inicial=="c" and final=="f":
    Cel=int(input("Temperatura en °C:"))
    print ("Temperatura en °F: ", CaF(Cel))
elif inicial=="c"and final=="k":
    Cel=int(input("Temperatura en °C:"))
    print ("Temperatura en K: ", CaK(Cel))
elif inicial=="c" and final=="r":
    Cel=int(input("Temperatura en °C:"))
    print ("Temperatura en R: ", CaR(Cel))
