'''  ejercicio desarrolle un programa que permita ingresar 5 numeros y 
al finalizar retorne cuantos numero pares ingreso el ux 
nota: solo deben considerar numeros positivos, el programa debe validar que el numero
 ingresado sea positivo, si el numero es negativo debe mostrar un
 mensaje de error y no contar ese numero como parte de los 5 numeros a ingresar.
 esto con el ciclo for '''


for ciclo in range (0, 5, 1):
     n = int ( input("ingresa  un numero positivo :"))
     if n < 0:
            print("error, el numero ingresado es negativo, por favor ingresa un numero positivo")
        

