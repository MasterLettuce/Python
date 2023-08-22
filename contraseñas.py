'''
* Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
* Podrás configurar generar contraseñas con los siguientes parámetros:
* - Longitud: Entre 8 y 16.
* - Con o sin letras mayúsculas.
* - Con o sin números.
* - Con o sin símbolos.
* (Pudiendo combinar todos estos parámetros entre ellos)
'''

import random as rd 
lon=10 #int(input("Caracteres de la contraseña entre 8 y 16: "))

'''lon=rd.randint(8,16)'''
a=0
i=0
if 8<=lon<=16:
	for i in range(1,(lon)):
		rand=rd.randint(48,122)
		i+=1
		a=chr(rand)+str(a)
	print ("Contraseña de "+str(lon)+" caracteres: "+ a)
else:
	print ("Debe ser entre 8 y 16 caracteres")

