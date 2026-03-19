# clases padre (super clases) e hijas . Las clases padres tienen las caracteristicas comunes y las hijas las caracteristicas especificas de cada una
class Animal:
  def comer(self):
    print("Como muchas veces al dia")
    
  def dormir(self):
    print("Duermo muchas horas al dia")
    
class Perro(Animal):
  
  def hacer_sonido(self):
    print("Puede Ladrar")
    
  # Puede acceder a los metodos de la clase padre
  
print("Ejemplo de herencia en python")

animal1 = Animal()
animal1.comer()
animal1.dormir()

print("\nClase Hija, soy un perro")
perro1 = Perro()
perro1.comer()
perro1.hacer_sonido()