from lib import cuadrado, rectangulo, triangulo, circunferencia
print("Proyecto Figuras")
lado=4
print(f"El área de un {cuadrado.get_identificador()} de lado {lado} es: {cuadrado.get_area(lado)} y el perímetro es {cuadrado.get_perimetro(lado)}")

base=4
altura=2
lado_a=2
lado_b=5
lado_c=3
print(f"El área de un {rectangulo.get_identificador()} de base {base} y altura {altura} es: {rectangulo.get_area(base,altura)} y el perímetro es: {rectangulo.get_perimetro(base,altura)}")

print(f"El área de un {triangulo.get_identificador()} de base {base} y altura {altura} es: {triangulo.get_area(base,altura)} y el perímetro es {triangulo.get_perimetro(lado_a, lado_b, lado_c)}")


radio=3
print(f"El área de la circunferencia de radio {radio} es {circunferencia.get_area(radio)}")