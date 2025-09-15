####################
## EJERICIO 5
# Escribe un programa que valide un DNI español se deben hacer dos comprobaciones:
#   Que el número tenga 8 dígitos y la letra sea una letra válida.
#   Que la letra corresponda con el número según la tabla oficial ("TRWAGMYFPDXBNJZSQVHLCKE"),
#   siendo la letra, la posición correspondiente con el número, módulo 23.
####################
def validar_dni(dni: str) -> bool:
    """
    Valida un DNI español (8 dígitos + letra).
    Acepta formato con o sin espacios.
    Args:
        dni (str): Dni a validar
    Returns:
        boolean: True, si es valido, False si no lo es.
    """
    # TODO: Usa la variable dni y convierte todo el texto en mayúsculas
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    resultado = False

    # TODO: Comprueba que la longitud de dni sera 9
    #    return resultado

    numero = int(dni[:-1])
    letra_dni = dni[-1]

    # TODO: Usa la variable letra_correcta, el valor en la cadea letras, cuya posición sera el resto de la divisón entre 23. (módulo 23)

    # TODO: Comprueba que letra_dni sea igual que letra_correcta.
    #    resultado = True

    return resultado


# Ejemplos de uso
if __name__ == "__main__":

    print(validar_dni("12345678Z"))  # ✅ True
    print(validar_dni("12345678A"))  # ❌ False

    dni_a_validar = input("Introduce DNI a validar:")
    print(validar_dni(dni_a_validar))
