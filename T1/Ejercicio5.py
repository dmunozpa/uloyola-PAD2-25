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
    dni = dni.upper().replace(" ", "")
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    resultado = False

    if len(dni) != 9:
        return resultado

    numero = int(dni[:-1])
    letra_dni = dni[-1]

    letra_correcta = letras[numero % 23]

    if letra_dni == letra_correcta:
        resultado = True

    return resultado


# Ejemplos de uso
if __name__ == "__main__":

    print(validar_dni("12345678Z"))  # ✅ True
    print(validar_dni("12345678A"))  # ❌ False

    dni_a_validar = input("Introduce DNI a validar:")
    print(validar_dni(dni_a_validar))
