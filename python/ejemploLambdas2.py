listadoNumeros = {5,623,23,100,21};
'''
listadoNumeros.append("Nombre")
listadoNumeros.append(True)
print(listadoNumeros);
'''

a = {1,3,3,3,3,3,3,3,3,3,3,3,3}
a.add(6)
print(a)

b = {1,5,7};
c = a | b;#union entre b y a
print(c);
c = a & b;#interseccion entre b y a
print(c);

sumar = lambda numero1, numero2 : numero1 + numero2;
#Filtros
condicion = lambda numero : numero >= 100;
listadoNumerosIgualesA5 = set(filter(condicion,listadoNumeros))
print(listadoNumerosIgualesA5);

