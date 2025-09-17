####################
## EJERICIO 5
# Escribe un programa que valide un DNI español se deben hacer dos comprobaciones: 
#    Valida con una función el número tenga 8 dígitos  
#    Valida con una función que la letra sea una letra válida. 
# La letra corresponda con el número según la tabla oficial ("TRWAGMYFPDXBNJZSQVHLCKE"). 
#Siendo la letra, la posición correspondiente con el resto del módulo 23. 
####################
def valida_9_digitos(dni:str)->bool:
    """
    Función que valida que un dni tiene 9 dígitos.
    Args:
        dni (str): String de entrada

    Returns:
        bool: True / False
    """
    
    resultado = False
    
    # TODO: Condición para evaluar que la longitud de la cadena es igual que 9.
    #    resultado = True
    
    return resultado

def valida_letra_dni(dni:str)->bool:
    """
    Función que valida que la letra de un DNI sea la correcta, revisando la letra que coincida con el resto % 23, de la posición en la tabla
    Tabla: "TRWAGMYFPDXBNJZSQVHLCKE"
    Args:
        dni (str): String de entrada

    Returns:
        bool: True / False
    """
    dni = dni.upper().replace(" ", "")
    resultado = False
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    
    # TODO: Usamos la variable numero, para coger la parte del numérica del DNI.
    # TODO: Usamos la variable letra_dni, para coger la parte de la letra del DNI.

    # TODO: usamos la variable letra_correcta, con la posición de la letra en la variable letras, siendo la posición % 23.
    
    if letra_dni == letra_correcta:
        resultado = True
        
    return resultado


def validar_dni(dni: str) -> bool:
    """
    Valida un DNI español (8 dígitos + letra).
    Acepta formato con o sin espacios.
    Args:
        dni (str): Dni a validar
    Returns:
        boolean: True, si es valido, False si no lo es.
    """
    resultado = False
    
    if valida_9_digitos(dni=dni) is False :
        print("❌ El DNI no tiene 9 letras")
        return resultado
    elif valida_letra_dni(dni=dni) is False :
        print("❌ La letra del DNI no es la correcta")
        return resultado
    else:
        print("✅ DNI es válido")
        resultado = True

    return resultado


# Ejemplos de uso
if __name__ == "__main__":

    validar_dni("12345678Z")  # ✅ True
    validar_dni("12345678A")  # ❌ False

    dni_a_validar = input("Introduce DNI a validar:")
    validar_dni(dni_a_validar)
    
    
