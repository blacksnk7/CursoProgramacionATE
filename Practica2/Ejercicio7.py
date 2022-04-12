nota1 = int(input("Ingrese la primer nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercer nota: "))
promedio = (nota1 + nota2 + nota3) / 3 #Calculamos el promedio entre las 3 notas.
if (promedio >= 8) and (nota1 >= 6) and (nota2 >= 6) and (nota3 >= 6): #Aca preguntamos primero si el promedio es mayor o igual que 8. Despues, tenemos varios "and", un "and" es como decir "y" en castellano. Lo que hacemos es preguntar si el promedio es mayor o igual que 8 Y ADEMAS la primera nota es mayor o igual que 6 Y ADEMAS.... asi con las tres notas. En caso de que TODAS las preguntas sean ciertas, entonces el if ejecutara el codigo indentado. Conque solo UNA pregunta nos de falso, el codigo indentado no se ejecutara.
    print("El/La alumno/a promociona!")
else:
    print("El/La alumno/a NO promociona. :(")