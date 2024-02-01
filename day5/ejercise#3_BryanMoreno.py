#balls

import math

class Esfera:
    def __init__(self, x, y, z, r):
        self.x = x
        self.y = y
        self.z = z
        self.r = r # radio de la esfera

    def distancia_a_esfera(self, otra_esfera):
        # distancia entre los centros de las dos esferas
        distancia = math.sqrt((self.x - otra_esfera.x)**2 + (self.y - otra_esfera.y)**2 + (self.z - otra_esfera.z)**2)
        # suma de los radios de las dos esferas
        suma_radios = self.r + otra_esfera.r
        # verificamos si la distancia es menor o igual a la suma de los radios
        if distancia <= suma_radios:
            return True
        else:
            return False

# ejemplo de uso
esfera1 = Esfera(0, 0, 0, 5)
esfera2 = Esfera(10, 0, 0, 3)

if esfera1.distancia_a_esfera(esfera2):
    print("Las esferas se tocan o se superponen.")
else:
    print("Las esferas no se tocan ni se superponen.")