from src.numeros import factorial

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(3) == 6
