def mi_chicha(a,b,c):
	disc=(b**2) -(4.0*a*c)
	x1= (-b+(disc**(1/2)))/(2*a)
	x2= (-b-(disc**(1/2)))/(2*a)
	return (x1,x2)


print('Elaboración de programación para resolver ecuaciones de segundo grado de la forma Ax^2+Bx+C')

print('indica los valores de los coeficientes')
print('A')
a=int(input())
print('B')
b=int(input())
print('C')
c=int(input())
print('----------------')
print('valor de X1 y X2:', mi_chicha(a,b,c))
