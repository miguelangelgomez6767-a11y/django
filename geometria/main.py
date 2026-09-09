from esfera import Esfera
from cilindro import Cilindro
from cubo import Cubo


esfera = Esfera(5)
cilindro = Cilindro(4, 10)
cubo = Cubo(6)


print("VOLUMEN DE LAS FIGURAS")

print("Esfera:", esfera.calcular_volumen())
print("Cilindro:", cilindro.calcular_volumen())
print("Cubo:", cubo.calcular_volumen())