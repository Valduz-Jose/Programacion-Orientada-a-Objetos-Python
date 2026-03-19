# Se pueden modificar los métodos de la clase padre en la clase hija, esto se llama sobrescritura de métodos. Esto permite que la clase hija tenga un comportamiento diferente al de la clase padre para un método específico.

class Animal:
  def comer(self):
    print("Como muchas veces al dia")
    
  def dormir(self):
    print("Duermo muchas horas al dia")
    
class Perro(Animal):
  
  def hacer_sonido(self):
    print("Puede Ladrar")
    
  # sobreescritura del metodo dormir
  def dormir(self):
    print("Duermo 15 horas al dia")
    
  
print("Ejemplo de sobrescritura en python")

animal1 = Animal()
animal1.comer()
animal1.dormir()

print("\nClase Hija, soy un perro")
perro1 = Perro()
perro1.comer()
perro1.dormir() # se ejecuta el metodo dormir de la clase Perro, no el de la clase Animal
perro1.hacer_sonido()