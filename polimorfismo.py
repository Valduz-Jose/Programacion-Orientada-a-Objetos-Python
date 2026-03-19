# Se pueden modificar los métodos de la clase padre en la clase hija, esto se llama sobrescritura de métodos. Esto permite que la clase hija tenga un comportamiento diferente al de la clase padre para un método específico.

class Animal:
    
  def hacer_sonido(self):
    print("Hago un sonido")
    
class Perro(Animal):
  
  def hacer_sonido(self):
    print("Puede Ladrar")
  
class Gato(Animal):
  
  def hacer_sonido(self):
    print("Puede Maullar")
    
    
print("Ejemplo de Polimorfismo en python")

animal1 = Animal()
animal1.hacer_sonido()

perro1 = Perro()
perro1.hacer_sonido()

gato1 = Gato()
gato1.hacer_sonido()

# Multiples comportamientos con el mismo metodo, esto se llama polimorfismo. El mismo metodo puede tener diferentes comportamientos dependiendo de la clase a la que pertenezca el objeto que lo llama.