# La clase Object es la clase padre de todas las clases en python, todas las clases heredan de la clase Object. La clase Object tiene algunos metodos predefinidos que pueden ser sobrescritos por las clases hijas, como el metodo __str__ que se utiliza para representar un objeto como una cadena de texto.
# Tambien el __init__ es un metodo predefinido que se utiliza para inicializar los atributos de un objeto, este metodo se llama automaticamente cuando se crea un objeto de una clase.
# tecnicamente siempre de estan sobreescribiendo los metodos de la clase Object, pero no es necesario hacerlo si no se necesita un comportamiento diferente al que ya tiene la clase Object.
class Persona:
  def __init__(self,nombre,apellido):
    self.nombre = nombre
    self.apellido = apellido
    
  # sobreescribir el metodo __str__
  def __str__(self):
    return f'''Persona:
    Nombre: {self.nombre}
    Apellido: {self.apellido}
    Dir. mem. {super.__str__(self)}'''#Se hace uso de super() para llamar al metodo __str__ de la clase Object, que devuelve una cadena con el nombre de la clase y la direccion de memoria del objeto. Esto se hace para mostrar la direccion de memoria del objeto junto con la informacion del objeto.
    
    # por defecto imprime la direccion de memoria del objeto, pero al sobrescribir el metodo __str__ se puede imprimir una cadena de texto con la informacion del objeto.
    
# Principal
persona1 =Persona("Ana","Martinez")
print(persona1) # se llama al metodo __str__ de la clase Persona, no al de la clase Object, porque se ha sobrescrito el metodo __str__ en la clase Persona. Si no se hubiera sobrescrito el metodo __str__, se llamaria al metodo __str__ de la clase Object, que devuelve una cadena con el nombre de la clase y la direccion de memoria del objeto.
