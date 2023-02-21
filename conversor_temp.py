#conversor de temperaturas
CaK=lambda:x+273.15
CaF=lambda:x*(9/5)+32
CaR=lambda:x*(9/5)+491.67

KaC=lambda:x-273.15
KaF=lambda:(x-273.15) * (9/5) + 32 
KaR=lambda:x*1.8

FaC=lambda:(x-32)*5/9
FaK=lambda:(x-32)*5/9+273.15 
FaR=lambda:x+459.67

RaC=lambda:(x-491.67)*5/9
RaK=lambda:x/1.8 
RaF=lambda:x-459.67

print(" Escalas de temperatura Celcius(c),Farenheit(f), Kelvin(k), Rankine(r)")
print("Indica la escala que tienes:")
inicial=input()
print("Indica la escala que deseas:")
final=input()

if inicial=="c":
    x=float(input("Temperatura en °C:"))
    if inicial=="c" and final=="f":
        print ("Temperatura en °F: ", CaF())
    elif inicial=="c"and final=="k":
        print ("Temperatura en K: ", CaK())
    elif inicial=="c" and final=="r":
        print ("Temperatura en R: ", CaR())

if inicial=="k":
    x=float(input("Temperatura en K:"))
    if inicial=="k" and final=="c":
        print ("Temperatura en °C: ", KaC())
    elif inicial=="k"and final=="f":
        print ("Temperatura en °F: ", KaF())
    elif inicial=="k" and final=="r":
        print ("Temperatura en R: ", KaR())

if inicial=="f":
    x=float(input("Temperatura en °F:"))
    if inicial=="f" and final=="c":
        print ("Temperatura en °C: ", FaC())
    elif inicial=="f"and final=="k":
        print ("Temperatura en K: ", FaK())
    elif inicial=="f" and final=="r":
        print ("Temperatura en R: ", FaR())

if inicial=="r":
    x=float(input("Temperatura en R:"))
    if inicial=="r" and final=="c":
        print ("Temperatura en °C: ", RaC())
    elif inicial=="r"and final=="k":
        print ("Temperatura en K: ", RaK())
    elif inicial=="r" and final=="f":
        print ("Temperatura en °F: ", RaF())
