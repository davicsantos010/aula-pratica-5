ROMANOS = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

def romano_para_decimal(romano: str) -> int:
    total = 0
    anterior = 0
    for c in reversed(romano.upper()):
        valor = ROMANOS.get(c, 0)
        if valor < anterior:
            total -= valor
        else:
            total += valor
        anterior = valor
    return total
