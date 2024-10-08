def get_area(base, altura):
    return base*altura
def get_identificador():
    return "rectángulo"
def get_perimetro(base, altura):
    return (base+altura)*2

resultado=get_area(2,3)
perimetro=get_perimetro(2,3)
identificador=get_identificador()
print("El área es: ",resultado)
print("El perímetro es: ",perimetro)
print("Es un: ", identificador)