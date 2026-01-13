valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Taxa do dólar: R$ {taxa_dolar:.2f}")
print(f"Taxa do euro: R$ {taxa_euro:.2f}")
print(f"Convertido para dólar: US$ {valor_dolar:.2f}")
print(f"Convertido para euro: € {valor_euro:.2f}")
