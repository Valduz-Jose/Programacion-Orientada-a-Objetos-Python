# Funcion Polimorfica
class Animal:
    
  def hacer_sonido(self):
    print("Hago un sonido")
    
class Perro(Animal):
  
  def hacer_sonido(self):
    print("Puede Ladrar")
  
class Gato(Animal):
  
  def hacer_sonido(self):
    print("Puede Maullar")
    
# Funcion Polimorfica
def hacer_sonido_animal(animal):
  animal.hacer_sonido()
# El tipo de dato del objeto que se le pasa a la funcion no importa, lo importante es que el objeto tenga el metodo hacer_sonido, esto se llama duck typing. El mismo metodo puede tener diferentes comportamientos dependiendo de la clase a la que pertenezca el objeto que lo llama.
# Si parece un pato, nada como un pato y hace sonido de pato, entonces es un pato. Si el objeto tiene el metodo hacer_sonido, entonces se puede llamar a ese metodo sin importar el tipo de dato del objeto.

print("Ejemplo de Polimorfismo en python")

animal1 = Animal()
hacer_sonido_animal(animal1)

perro1 = Perro()
hacer_sonido_animal(perro1)

gato1 = Gato()
hacer_sonido_animal(gato1)

