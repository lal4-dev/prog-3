class PersonaAdulta:
    # __init__(self, nombre, edad): Este es el método especial llamado constructor.
    # Se utiliza para inicializar los atributos de la clase cuando se crea una nueva instancia.
    # En este caso, establece los atributos nombre y edad con los valores proporcionados.
    def __init__(self, nombre, edad):
        # El parámetro self se refiere al objeto actual que se está creando a partir de la clase.
        # Atributos de la Clase:
        self.nombre = nombre  # Almacena el nombre de la persona.
        self.edad = edad  # Almacena la edad de la persona.

    # Este método imprime un saludo que incluye el nombre y la edad de la persona. Los métodos de clase ,
    # son funciones que pertenecen a una clase y pueden ser ejecutados por los objetos de esa clase.
    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años.')


# Instanciación: para crear un objeto, necesitamos instanciar una clase.
# La instancia es una representación concreta de la clase.
persona1 = PersonaAdulta("Felipe", 18)

# Llamar al método saludar
persona1.saludar()
