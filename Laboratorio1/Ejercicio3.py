
def generate_pass(prefix, start, end):
    if (start > end):
        print('El comienzo del DNI es mayor que el final.')
    else:
        if (len(start) > 8):
            start = start[-8:]
            end = end[-8:]
        elif (len(end) > 8):
            end = end[-8:]
        real_start = (int(prefix)*10000000000) + int(start)
        real_end = (int(prefix)*10000000000) + int(end)
    for num in range(real_start, real_end):
        print(prefix + str(num)[-8:])

prefix = ['004', '011', '044']
choice = int(input(f'Ingrese el prefijo a utilizar: \n1 - {prefix[0]} \n2 - {prefix[1]} \n3 - {prefix[2]}\n'))
start = input('Ingrese el numero desde el que se quiera comenzar a generar: ')
end = input('Ingrese el numero hasta el cual se quiera generar: ')
generate_pass(prefix[choice], start, end)