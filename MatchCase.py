def opciones(opcion):
    match opcion:
        case "A":
            return "Una opcion"
        case "B":
            return "Otra opcion"
        case "C":
            return "Otra opcion"
        case _:
            return "Ninguna de las opciones"
        
print(opciones("I")) 