import math

def main():
    """
    Este ejercicio encuentra el valor de la hipotenusa de un triangulo rectangulo, dados dos catetos
    """

    cateto_1 = float(input("Ingrese la longitud del primer cateto en centímetros: "))
    cateto_2 = float(input("Ingrese la longitud del segundo cateto en centímetros: "))

    hipotenusa = math.sqrt(math.pow(cateto_1,2) + math.pow(cateto_2,2))

    print(f"La hipotenusa del triángulo rectángulo es {hipotenusa:.3f} cm")

if __name__=='__main__':
    main()
