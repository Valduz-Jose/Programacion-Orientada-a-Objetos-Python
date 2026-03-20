from computadora import Computador
from orden import Orden
from monitor import Monitor
from teclado import Teclado
from raton import Raton

print("MUNDO PC")

teclado1 = Teclado("HP", "USB")
raton1 = Raton("Logitech", "USB")
monitor1 = Monitor("Samsung", "27 pulgadas")
computadora1 = Computador("HP", monitor1, teclado1, raton1)
# print(computadora1)
  
teclado2 = Teclado("Gamer", "USB")
raton2 = Raton("Logitech", "USB")
monitor2 = Monitor("SnapDragon", "27 pulgadas")
computadora2 = Computador("Gamer", monitor2, teclado2, raton2)
# print(computadora2)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
# print(orden1)

teclado3 = Teclado("Logitech", "USB")
raton3 = Raton("Logitech", "USB")
monitor3 = Monitor("LG", "27 pulgadas")
computadora3 = Computador("LG", monitor3, teclado3, raton3)
orden1.agregar_computadora(computadora3)
print(orden1)