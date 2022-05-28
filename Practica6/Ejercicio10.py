empleados = ['Agustina', 'Juan Manuel', 'Martina']
defaults = {"Puesto": 'Developer', "Salario": 1200}
new_dicc = {}
for name in empleados:
    new_dicc[name] = defaults
print(new_dicc)