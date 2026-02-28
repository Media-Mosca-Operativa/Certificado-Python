def evaluar_color(color):
    match color:
        case "rojo":
            return "Color de alerta"
        case "verde":
            return "Color de aceptación"
        case _:
            return "Color desconocido"

print(evaluar_color("rojo"))
print(evaluar_color("azul"))