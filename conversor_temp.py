#conversor de temperaturas
CaK=lambda:x+273.15
CaF=lambda:x*(9/5)+32
CaR=lambda:x*(9/5)+491.67

print(" Escalas de temperatura Celcius(c),Farenheit(f), Kelvin(k), Rankine(r)")
print("Indica la escala que tienes:")
inicial=input()
print("Indica la escala que deseas:")
final=input()

if inicial=="c" and final=="f":
    x=int(input("Temperatura en °C:"))
    print ("Temperatura en °F: ", CaF())
elif inicial=="c"and final=="k":
    x=int(input("Temperatura en °C:"))
    print ("Temperatura en K: ", CaK())
elif inicial=="c" and final=="r":
    x=int(input("Temperatura en °C:"))
    print ("Temperatura en R: ", CaR())
