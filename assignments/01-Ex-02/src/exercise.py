import math

def main():
    """
    Este ejercicio calcula el volumen de un octaedro
    """

    arista = float(input("Introduce la longitud de la arista del octaedro en centímetros:"))

    volumen = math.sqrt(2) / 3 * math.pow(arista,3)

    print(f"El volumen del octaedro es: {volumen:.4f} cm3")

if __name__=='__main__':
    main()
