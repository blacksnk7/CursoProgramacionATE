import os
import Ejercicio1 as e1
import Ejercicio2 as e2
import Ejercicio3 as e3
import Ejercicio4 as e4
import Ejercicio5 as e5
import Ejercicio6 as e6
import Ejercicio7 as e7
import Ejercicio8 as e8
import Ejercicio9 as e9
import Ejercicio10 as e10


file_path = os.path.join(os.getcwd(), 'text')
e1.print_file(file_path)
n = int(input('Ingrese la cantidad de lineas del archivo a leer: '))
e2.print_lines(file_path, n)
e3.count_M(file_path)
e4.count_words(file_path)
word = input('Ingrese una palabra a buscar en el archivo: ')
e5.count_times(file_path, word)
e6.short_words(file_path)
e7.count_upper(file_path)
old_word = input('Ingrese la palabra que desea reemplazar: ')
new_word = input('Ingrese una nueva palabra para reemplazar la anterior: ')
e8.exchange_words(file_path, old_word, new_word)
e9.create_new_file(file_path)
e10.capitalize_file(file_path)