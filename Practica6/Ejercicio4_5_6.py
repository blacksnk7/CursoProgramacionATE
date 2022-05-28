diccionario = {
    "clase": {
        "estudiante": {
            "nombre": "Marcos",
            "materias": {
                "matematica": 7,
                "geografia": 8
            }
        }
    }
}
print(diccionario["clase"]["estudiante"]["materias"]["geografia"])
diccionario["clase"]["estudiante"]["materias"]["geografia"] = 7
diccionario["clase"]["estudiante"]["materias"]["matematica"] = 8
diccionario["clase"]["estudiante"]["materias"]["historia"] = 7
diccionario["clase"]["estudiante"]["materias"].pop("geografia")
print(diccionario)