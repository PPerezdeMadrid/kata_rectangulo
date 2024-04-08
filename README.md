# Katas 

## Credenciales
Si tienes que meter el nombre y la contraseña con cada git push:

```Python
    git config --global credential.helper cache
    git config --global credential.helper 'cache --timeout=18000'

```
## Unittest

1. **Importar `unittest`**: Comienza importando el módulo `unittest`.

```python
import unittest


class MyTestCase(unittest.TestCase):
    # Define métodos de prueba aquí
    def test_suma(self):
        self.assertEqual(2 + 2, 4)

    def test_resta(self):
        self.assertEqual(5 - 3, 2)
```

Ejecutar las pruebas:
```bash
python -m unittest nombre_del_archivo.py
```

```makefile
# Makefile para un proyecto de Python

.PHONY: test clean

test:
    python -m unittest test.py

clean:
    rm -rf __pycache__ *.pyc
```

### Ejemplo completo:

```python
import unittest

# La clase de prueba
class MyTestCase(unittest.TestCase):
    # Método de prueba
    def test_suma(self):
        self.assertEqual(2 + 2, 4)

    def test_resta(self):
        self.assertEqual(5 - 3, 2)
        
if __name__ == '__main__':
    unittest.main()
```


