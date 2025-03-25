from src.operaciones_extra import elevar_al_cuadrado, es_par

def test_elevar_al_cuadrado():
    assert elevar_al_cuadrado(3) == 9
    assert elevar_al_cuadrado(0) == 0

def test_es_par():
    assert es_par(4) == True
    assert es_par(7) == False
