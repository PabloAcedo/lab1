# la secuencia de bytes para este archivo se introduce por command line
# ejemplo de ejecucion del programa:
# entrada a command line(ubuntu): python3 run-length-encode.py 12345
# donde 12345 es la secuencia de entrada

import collections as col
import sys

def run_length_encode(data):
    # crear diccionario vacio con todos los simbolos en la secuencia de entrada
    sym = col.OrderedDict.fromkeys(data, 0)

    # recorrer la secuencia de simbolos y guardar en el diccionario cuantos simbolos existen de cada tipo
    for i in data:
        sym[i] += 1

    # crear secuencia de salida (secuencia codificada con run length)
    result = ''
    for i, j in sym.items():
        result += str(i) + str(j)

    return result


print('\nSecuencia de entrada:', sys.argv[1], '->', 'Secuencia codificada con run length',
      run_length_encode(sys.argv[1]), '\n')
