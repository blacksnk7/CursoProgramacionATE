temp = {
    'domingo': 23.3,
    'lunes': 22.6,
    'martes': 18.9,
    'miercoles': 17.2,
    'jueves': 19.4,
    'viernes': 20.0,
    'sabado': 24.1
}

min = 999
for key in temp:
    if (temp[key] <= min):
        min = temp[key]
        min_day = key
print(f"El dia con menor temperatura fue el {min_day} con una temperatura de: {temp[min_day]} grados")