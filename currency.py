"""
Test!

No functions longer than 7 lines of code
"""

def get_rate(rates, original_currency, to):
    rate = 0
    if [rate for origin, dest, rate in rates
        if (origin == original_currency and dest == to)][0]:
            return rate
    elif [rate for origin, dest, rate in rates
        if (origin == to and dest == original_currency)][0]:
            return rate
    else:
        return 0



def same_rate(original_currency, to):
    if original_currency == to:
        return True
    else:
        return False

def convert(rates, value, original_currency, to):
    if same_rate(original_currency, to):
        return value
    return value * get_rate(rates, original_currency, to)

if __name__ == '__main__':
    rates = [("USD", "EUR", 0.866)
             ("EUR", "USD", 1.154)
             ("EUR","JPY", 0.007)
             ("JPY","EUR", 137.20)]
    convert(rates,1,"USD","EUR")
