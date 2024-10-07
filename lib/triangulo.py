def get_area(base, altura):
    return (base*altura)/2
def get_identificador():
    return "triángulo"
def get_perimetro(lado_a, lado_b, lado_c):
    return lado_a+lado_b+lado_c

resultado=get_area(2, 3)
perimetro=get_perimetro(2,4,5)
identificador=get_identificador()
print("El área es: ",resultado)
print("El perímetro es: ",perimetro)
print("Es un: ", identificador)