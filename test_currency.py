from currency import *

rates = [("USD", "EUR", 0.866),
         ("EUR", "USD", 1.154),
         ("EUR","JPY", 0.007),
         ("JPY","EUR", 137.20)]

def test_convert_same_currency():
    assert convert(rates,12,"USD","USD") == 12
    assert convert(rates,0.12,"EUR","EUR") == 0.12

def test_convert_easy_convert():
    assert convert(rates,1,"USD","EUR") == 0.866
    assert convert(rates,1,"EUR","JPY") == 0.007
