def saludar(nombre_completo):
    """
    Retorna un saludo personalizado.
    Parámetros:
        nombre_completo (str): Nombre de la persona a saludar.
    """
    if not nombre_completo or nombre_completo.strip() == "":
        return "Error: el nombre no puede estar vacío."
    return f"Hola, {nombre_completo}!"

print(saludar("GitHub"))
