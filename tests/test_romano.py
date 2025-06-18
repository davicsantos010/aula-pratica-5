from src.romano import romano_para_decimal

def test_simples():
    assert romano_para_decimal("I") == 1
    assert romano_para_decimal("V") == 5
    assert romano_para_decimal("X") == 10

def test_combinacoes():
    assert romano_para_decimal("IV") == 4
    assert romano_para_decimal("IX") == 9
    assert romano_para_decimal("XL") == 40
    assert romano_para_decimal("XC") == 90

def test_complexos():
    assert romano_para_decimal("MCMXCIV") == 1994
    assert romano_para_decimal("MMXXV") == 2025

def test_minusculas():
    assert romano_para_decimal("xiv") == 14
    assert romano_para_decimal("mmxxv") == 2025

def test_invalido():
    assert romano_para_decimal("ABC") == 100 
