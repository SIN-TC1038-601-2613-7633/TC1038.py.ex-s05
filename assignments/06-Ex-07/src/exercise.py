import math

def main():
    """
    Este programa calcula el valor de la longitud del cateto opuesto dada la hipotenusa y un angulo de 30 grados
    """

    hipotenusa = float(input("Dame el valor de la hipotenusa:"))

    cateto_opuesto = math.sin(math.radians(30)) * hipotenusa

    print(f"Valor del cateto opuesto: {cateto_opuesto:.2f}")

if __name__=='__main__':
    main()
