import re

# Definir los patrones para los símbolos léxicos
patterns = [
    (r'\d+', 'ENTERO'),                         # Números enteros
    (r'\d+\.\d+', 'REAL'),                      # Números reales
    (r'[a-zA-Z_]\w*', 'IDENTIFICADOR'),         # Identificadores
    (r'\+', 'SUMA'),                            # Operador de suma
    (r'-', 'RESTA'),                            # Operador de resta
    (r'\*', 'MULTIPLICACION'),                  # Operador de multiplicación
    (r'/', 'DIVISION'),                         # Operador de división
    (r'=', 'ASIGNACION'),                       # Operador de asignación
    (r'<', 'MENOR_QUE'),                        # Operador relacional menor que
    (r'>', 'MAYOR_QUE'),                        # Operador relacional mayor que
    (r'<=', 'MENOR_IGUAL_QUE'),                 # Operador relacional menor o igual que
    (r'>=', 'MAYOR_IGUAL_QUE'),                 # Operador relacional mayor o igual que
    (r'!=', 'DIFERENTE_QUE'),                   # Operador relacional diferente que
    (r'==', 'IGUAL_QUE'),                       # Operador relacional igual que
    (r'&&', 'AND'),                             # Operador AND lógico
    (r'\|\|', 'OR'),                            # Operador OR lógico
    (r'!', 'NOT'),                              # Operador NOT lógico
    (r'\(', 'PARENTESIS_IZQ'),                  # Paréntesis izquierdo
    (r'\)', 'PARENTESIS_DER'),                  # Paréntesis derecho
    (r'{', 'LLAVE_IZQ'),                        # Llave izquierda
    (r'}', 'LLAVE_DER'),                        # Llave derecha
    (r';', 'PUNTO_Y_COMA'),                     # Punto y coma
    (r'\s+', None)                              # Espacios en blanco (ignorados)
]

# Función principal del analizador léxico
def lexer(input_text):
    tokens = []
    position = 0

    while position < len(input_text):
        match = None
        for pattern, token_type in patterns:
            regex = re.compile(pattern)
            match = regex.match(input_text, position)
            if match:
                value = match.group(0)
                if token_type:
                    tokens.append((token_type, value))
                break

        if not match:
            raise Exception(f"No se pudo analizar el texto en la posición {position}")

        position = match.end()

    return tokens

# Ejemplo de uso
if __name__ == "__main__":
    input_text = "if (x > 0) return x; else return -x;"
    tokens = lexer(input_text)

    print("Tokens generados:")
    for token_type, value in tokens:
        print(f"{token_type}: {value}")
import re

# Definir los patrones para los símbolos léxicos
patterns = [
    (r'\d+', 'ENTERO'),                         # Números enteros
    (r'\d+\.\d+', 'REAL'),                      # Números reales
    (r'[a-zA-Z_]\w*', 'IDENTIFICADOR'),         # Identificadores
    (r'\+', 'SUMA'),                            # Operador de suma
    (r'-', 'RESTA'),                            # Operador de resta
    (r'\*', 'MULTIPLICACION'),                  # Operador de multiplicación
    (r'/', 'DIVISION'),                         # Operador de división
    (r'=', 'ASIGNACION'),                       # Operador de asignación
    (r'<', 'MENOR_QUE'),                        # Operador relacional menor que
    (r'>', 'MAYOR_QUE'),                        # Operador relacional mayor que
    (r'<=', 'MENOR_IGUAL_QUE'),                 # Operador relacional menor o igual que
    (r'>=', 'MAYOR_IGUAL_QUE'),                 # Operador relacional mayor o igual que
    (r'!=', 'DIFERENTE_QUE'),                   # Operador relacional diferente que
    (r'==', 'IGUAL_QUE'),                       # Operador relacional igual que
    (r'&&', 'AND'),                             # Operador AND lógico
    (r'\|\|', 'OR'),                            # Operador OR lógico
    (r'!', 'NOT'),                              # Operador NOT lógico
    (r'\(', 'PARENTESIS_IZQ'),                  # Paréntesis izquierdo
    (r'\)', 'PARENTESIS_DER'),                  # Paréntesis derecho
    (r'{', 'LLAVE_IZQ'),                        # Llave izquierda
    (r'}', 'LLAVE_DER'),                        # Llave derecha
    (r';', 'PUNTO_Y_COMA'),                     # Punto y coma
    (r'\s+', None)                              # Espacios en blanco (ignorados)
]

# Función principal del analizador léxico
def lexer(input_text):
    tokens = []
    position = 0

    while position < len(input_text):
        match = None
        for pattern, token_type in patterns:
            regex = re.compile(pattern)
            match = regex.match(input_text, position)
            if match:
                value = match.group(0)
                if token_type:
                    tokens.append((token_type, value))
                break

        if not match:
            raise Exception(f"No se pudo analizar el texto en la posición {position}")

        position = match.end()

    return tokens

# Ejemplo de uso
if __name__ == "__main__":
    input_text = "if (x > 0) return x; else return -x;"
    tokens = lexer(input_text)

    print("Tokens generados:")
    for token_type, value in tokens:
        print(f"{token_type}: {value}")
