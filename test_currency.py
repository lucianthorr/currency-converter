from currency import *

rates = [("USD", "EUR", 0.866),
         ("EUR", "USD", 1.154),
         ("EUR","JPY", 0.007),
         ("JPY","EUR", 137.20)]

def test_convert_same_currency():
    assert convert(rates,12,"USD","USD") == 12
    assert convert(rates,0.12,"EUR","EUR") == 0.12

def test_easy_convert():
    assert convert(rates,1,"USD","EUR") == 0.866
    assert convert(rates,1,"EUR","JPY") == 0.007

def test_euro_to_dollar():
    assert convert(rates,1,"EUR","USD") == 1.154

def test_larger_convert():
    assert convert(rates,50,"USD","EUR") == 43.3
    assert convert(rates,25,"EUR","JPY") == 0.175

def test_get_same_rate():
    assert same_rate("USD", "USD") == True

def test_bad_rate():
    assert convert(rates,1,"CZK","DNM") == 0
