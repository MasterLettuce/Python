'''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 '''
def multi_3(num3):
	x=num3%3
	return x 

def multi_5(num5):
	x=num5%5
	return x
inicio=1
fin=101
i=0

for i in range(inicio,fin): 
	if multi_3(i)==0 and multi_5(i)==0:
		print("Fizzbuzz")
	else:
		if multi_3(i)==0:
			print("Fizz")
		else:
			if multi_5(i)==0:
				print("Buzz")
			else:
				print(i)
i += 1
print("-----------------")