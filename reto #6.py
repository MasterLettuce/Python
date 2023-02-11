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
    n_Jugadas=5
    for i in range(1,n_Jugadas+1):
        player1=rd.choice(formas)
        player2=rd.choice(formas)
        partidas=(player1,player2)
        return partidas
        i+=1
        
print(juego())      
