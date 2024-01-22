import re

def analizador_lexico(codigo):
    tokens = []
    patron_identificador = re.compile(r'[a-zA-Z][a-zA-Z0-9]*')
    patron_numero_real = re.compile(r'\d+\.\d+')

    while codigo:
        codigo = codigo.lstrip()  # Ignorar espacios en blanco al principio

        # Identificador
        match_id = patron_identificador.match(codigo)
        if match_id:
            tokens.append(("IDENTIFICADOR", match_id.group()))
            codigo = codigo[match_id.end():]
            continue

        # Número real
        match_real = patron_numero_real.match(codigo)
        if match_real:
            tokens.append(("NUMERO_REAL", match_real.group()))
            codigo = codigo[match_real.end():]
            continue

        # Caracteres no reconocidos
        tokens.append(("DESCONOCIDO", codigo[0]))
        codigo = codigo[1:]

    return tokens

while True:
    # Ingresar código fuente desde la consola
    codigo_fuente = input("Ingrese el código fuente (o escriba 'salir' para terminar): ")

    if codigo_fuente.lower() == 'salir':
        break

    # Analizar y mostrar resultados
    tokens = analizador_lexico(codigo_fuente)
    print("Tokens:")
    for token in tokens:
        print(token)
