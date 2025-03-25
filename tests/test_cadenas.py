from src.cadenas import invertir_cadena, convertir_mayusculas

def test_invertir_cadena():
    assert invertir_cadena("hola") == "aloh"
    assert invertir_cadena("Python") == "nohtyP"

def test_convertir_mayusculas():
    assert convertir_mayusculas("hola") == "HOLA"
    assert convertir_mayusculas("prueba") == "PRUEBA"
