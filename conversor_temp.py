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
    
Cel=int(input("Temperatura en °C:"))
print ("Temperatura en °F: ", CaF(Cel))
print ("Temperatura en K: ", CaK(Cel))
print ("Temperatura en R: ", CaR(Cel))
