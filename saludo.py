def saludar(nombre_completo):
    if not nombre_completo or nombre_completo.strip() == "":
        return "Error: el nombre no puede estar vacío."
    return f"Hola, {nombre_completo}!"

print(saludar("GitHub"))
