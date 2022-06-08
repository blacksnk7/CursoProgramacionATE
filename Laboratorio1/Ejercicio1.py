import csv

#Esta funcion busca un ID dentro del diccionario creado a partir del archivo csv.
def search_id_dicc(ID, dicc):
    id_list = dicc['id']
    if (ID in id_list):
        pos = id_list.index(ID)
        for key in dicc:
            print(f'{key}: {dicc[key][pos]}')
    else:
        print(f'La ID: {ID} no se encuentra dentro del archivo.')
    
#Esta funcion busca un ID dentro del archivo csv.
def search_id_file(ID, file_name):
    with open(file_name, encoding='utf-8') as data:
        data.readline()
        text = csv.reader(data, delimiter=',')
        for row in text:
            if (ID in row):
                print(row)
    

with open('datos.csv', encoding='utf-8') as data:
    dicc = {}
    keys = data.readline().strip('\n').split(',')
    print(keys)
    for key in keys:
        
        dicc[key] = []
    text = csv.reader(data, delimiter=',')
    words = []
    for row in text:
        i = 0
        for key in dicc:
            dicc[key].append(row[i])
            i += 1
ID = input('Ingrese una ID para buscar: ')
search_id_dicc(ID, dicc)
search_id_file(ID, 'datos.csv')