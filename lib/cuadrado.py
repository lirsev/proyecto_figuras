def get_area(lado):
    return lado*lado
def get_identificador():
    return "cuadrado"
def get_perimetro(lado):
    return lado*4

resultado=get_area(2)
perimetro=get_perimetro(2)
identificador=get_identificador()
print("El área es: ",resultado)
print("El perímetro es: ",perimetro)
print("Es un: ", identificador)