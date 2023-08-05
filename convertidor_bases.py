import re

def calcular_residuos(num, base, residuos):
    division = num // base

    if division >= 0:
      residuo = num % base
      if residuo > 9:
        residuo = chr(residuo + 55) # Pasamos de num a char, e.g. 15 -> F (15 + 55 = 70 es F en ascii)
      residuos.append(str(residuo))

    if division == 0:
      return residuos

    return calcular_residuos(division, base, residuos)

def decimal_a_base(numero, base):
    residuos = []
    residuos = calcular_residuos(numero, base, residuos)
    residuos.reverse()
    return ''.join(residuos)

def base_a_decimal(numero, base):
    digitos = list(str(numero))
    total_digitos = len(digitos)
    suma = 0

    for i in range(total_digitos):
      digito = digitos[i]
      if not digito.isdigit():
        digito = ord(digito) - 55 # Pasamos de char a num, e.g. F -> 15 (70 - 55 = 15)
      suma += (base ** (total_digitos - i - 1)) * int(digito)

    return suma

def pasar_a_num(digito):
  if digito.isalpha():
    return ord(digito) - 55

  return int(digito)

def validar_base(base):
  if not base.isdigit() or int(base) <= 1 or int(base) > 36: # 10 digitos + 26 letras = 36 simbolos
      print("La base debe ser un número entero entre dos y treinta y seis.")
      return False
  return True

def validar_nomenclatura(base, numero):
    es_valido = True
    digitos = list(numero)

    for digito in digitos:
        if pasar_a_num(digito) >= int(base):  # La base 5 acepta símbolos del 0 al 4 (num debe ser < base)
            print(f"El simbolo '{digito.upper()}' no existe en la base {base}")
            es_valido = False

    return es_valido

def validar_conversion(base, numero):
    print("Validando conversión...")
    p = re.compile('[a-zA-Z]+')
    digitos = list(numero)

    for digito in digitos:
      if not p.match(digito) and not digito.isdigit():  # si no es letra ni numero, bai
        print(f"No se admiten caracteres especiales como '{digito}'")
        digitos
        return False

    return numero.upper() if validar_nomenclatura(base, numero) else False 

def main():
    print("Conversor de sistemas numéricos")
    print("Seleccione una de las opciones:")
    print("1) Base 10 a base 3")
    print("2) Base 10 a base 8")
    print("3) Base 10 a base 9")
    print("4) Base 10 a base 16")
    print("5) Base 10 a base 6")
    print("6) Base 10 a base 7")
    print("7) Base 8 a base 10")
    print("8) Base 16 a base 10")
    print("9) Base 9 a base 10")
    print("10) Personalizado...")

    opcion = input("Elija una opción: ")
    while not opcion.isdigit() or (int(opcion) < 1 or int(opcion) > 10):
      opcion = input("Ingrese una opción válida: ")

    base_1 = 10
    base_2 = 10

    match int(opcion):
      case 1:
          base_2 = 3
      case 2:
          base_2 = 8
      case 3:
          base_2 = 9
      case 4:
          base_2 = 16
      case 5:
          base_2 = 6
      case 6:
          base_2 = 7
      case 7:
          base_1 = 8
      case 8:
          base_1 = 16
      case 9:
          base_1 = 9
      case 10:
          base_1 = input("Base de la que se quiere convertir (base inicio): ")
          while not validar_base(base_1):
            base_1 = input("Ingrese una base inicio válida: ")

          base_2 = input("Base a la que se quiere convertir (base destino): ")
          while not validar_base(base_2):
            base_2 = input("Ingrese una base destino válida: ")

    numero = input("Ingresa el número a convertir: ")
    while not (numero := validar_conversion(base_1, numero)):  # Si es false, entra al loop. Si es truthy (fue un número válido), sale del loop y lo guardamos
      numero = input("Ingrese un número válido: ")

    print("Validación terminada.")
    print("Convirtiendo...")
    
    if (int(base_1) != 10):
      numero = base_a_decimal(int(numero), int(base_1))

    if (int(base_2) != 10):
      numero = decimal_a_base(int(numero), int(base_2))

    print(f"Número convertido: {numero}")

if __name__ == "__main__":
    main()