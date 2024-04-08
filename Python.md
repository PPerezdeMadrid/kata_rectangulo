# Apuntes de Python rápidos

```Python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

persona1 = Persona("Juan", 30)

# Acceder a los atributos de la instancia
print("Nombre:", persona1.nombre)
print("Edad:", persona1.edad)

# Llamar al método saludar() de la instancia
saludo = persona1.saludar()
print(saludo)
```

## Otras características avanzadas de Python

1. **Comprensiones de Listas, Conjuntos y Diccionarios**
   ```python
   cuadrados = [x**2 for x in range(10)]
   conjunto_pares = {x for x in range(10) if x % 2 == 0}
   diccionario_cuadrados = {x: x**2 for x in range(10)}
   ```

2. **Manejo de Excepciones**: Python tiene una sintaxis limpia y poderosa para manejar excepciones y errores en el código. Esto incluye las cláusulas `try`, `except`, `else` y `finally`.
   ```python
   try:
       resultado = 10 / 0
   except ZeroDivisionError:
       print("Error: División por cero")
   else:
       print("El resultado es:", resultado)
   finally:
       print("Finalizando...")
   ```

3. **Decoradores**: Los decoradores son una forma elegante de modificar o extender el comportamiento de funciones y métodos en Python. Pueden utilizarse, por ejemplo, para añadir funcionalidades de registro, control de acceso, o memoización.
   ```python
   def decorador(funcion):
       def wrapper(*args, **kwargs):
           print("Ejecutando función...")
           resultado = funcion(*args, **kwargs)
           print("Función ejecutada.")
           return resultado
       return wrapper

   @decorador
   def mi_funcion():
       print("Dentro de la función.")

   mi_funcion()
   ```

4. **Generadores**: Los generadores son funciones especiales que permiten generar valores de manera perezosa, es decir, generar valores sobre la marcha sin tener que almacenar todos los valores en la memoria. Esto es útil cuando trabajas con grandes cantidades de datos.
   ```python
   def generador_cuadrados(n):
       for i in range(n):
           yield i ** 2

   for x in generador_cuadrados(5):
       print(x)
   ```

