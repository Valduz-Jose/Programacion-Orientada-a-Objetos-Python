from monitor import Monitor
from teclado import Teclado
from raton import Raton

class Computador:
  contador_computadoras = 0
  
  def __init__(self,nombre,monitor,teclado,raton):
    Computador.contador_computadoras += 1
    self.id_computadora = Computador.contador_computadoras
    self.nombre = nombre
    self.monitor = monitor
    self.teclado = teclado
    self.raton = raton
    
  def __str__(self):
    return (f"Computadora: {self.nombre} - {self.id_computadora}\nMonitor: {self.monitor}, Teclado: {self.teclado}, Ratón: {self.raton}\n")
  
if __name__ == "__main__":
  teclado1 = Teclado("HP", "USB")
  raton1 = Raton("Logitech", "USB")
  monitor1 = Monitor("Samsung", "27 pulgadas")
  computadora1 = Computador("HP", monitor1, teclado1, raton1)
  print(computadora1)
  
  teclado2 = Teclado("Gamer", "USB")
  raton2 = Raton("Logitech", "USB")
  monitor2 = Monitor("SnapDragon", "27 pulgadas")
  computadora2 = Computador("Gamer", monitor2, teclado2, raton2)
  print(computadora2)