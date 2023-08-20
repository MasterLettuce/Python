...
 Crea un programa que calcule quien gana más partidas al piedra,
 papel, tijera, lagarto, spock.
 El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 La función recibe un listado que contiene pares, representando cada jugada.
 El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
  Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 ...

 import random as rd 

formas=('piedra', 'papel', 'tijera', 'lagarto', 'spock')

def juego():
    player1=rd.choice(formas)
    player2=rd.choice(formas)
    partidas=(player1,player2)
    return partidas
    i+=1

def comparacion():
    j1,j2=(juego())

    #opciones de piedra
    if j1=="piedra" and j2=="tijera":
        return(j1,j2,"jugador 1 gana")
    elif j1=="piedra" and j2== "lagarto":
        return(j1,j2,"jugador 1 gana")
    elif j1=="tijera" and j2=="piedra":
        return(j1,j2,"jugador 2 gana")
    elif j1=="lagarto" and j2=="piedra":
        return(j1,j2,"jugador 2 gana")
    elif j1=="piedra" and j2=="piedra":
        return(j1,j2,"empate")    
    #opciones de papel
    elif j1=="papel" and j2=="piedra":
        return(j1,j2,"jugador 1 gana")
    elif j1=="papel" and j2=="spock":
        return(j1,j2,"jugador 1 gana")
    elif j1=="piedra" and j2=="papel":
        return(j1,j2,"jugador 2 gana")
    elif j1=="spock" and j2=="papel":
        return(j1,j2,"jugador 2 gana")
    elif j1=="papel" and j2=="papel":
        return(j1,j2,"empate")
    #opciones de tijera
    elif j1=="tijera" and j2=="papel":
        return(j1,j2,"jugador 1 gana")
    elif j1=="tijera" and j2=="lagarto":
        return(j1,j2,"jugador 1 gana")
    elif j1=="papel" and j2=="tijera":
        return(j1,j2,"jugador 2 gana")
    elif j1=="lagarto" and j2=="tijera":
        return(j1,j2,"jugador 2 gana")
    elif j1=="tijera" and j2=="tijera":
        return(j1,j2,"empate")
    #opciones de lagarto
    elif j1=="lagarto" and j2=="papel":
        return(j1,j2,"jugador 1 gana")
    elif j1=="lagarto" and j2=="spock":
        return(j1,j2,"jugador 1 gana")
    elif j1=="spock" and j2=="lagarto":
        return(j1,j2,"jugador 2 gana")
    elif j1=="papel" and j2=="lagarto":
        return(j1,j2,"jugador 2 gana")
    elif j1=="lagarto" and j2=="lagarto":
        return(j1,j2,"empate")
    #opciones de spock
    elif j1=="spock" and j2=="tijera":
        return(j1,j2,"jugador 1 gana")
    elif j1=="spock" and j2=="piedra":
        return(j1,j2,"jugador 1 gana")
    elif j1=="tijera" and j2=="spock":
        return(j1,j2,"jugador 2 gana")
    elif j1=="piedra" and j2=="spock":
        return(j1,j2,"jugador 2 gana")
    elif j1=="spock" and j2=="spock":
        return(j1,j2,"empate")    


n_Jugadas=5
for i in range(1,n_Jugadas+1):
    i1,i2,i3=(comparacion())
    
    print(comparacion())
i+=1
