# Homework 5
# Jason Aylward


def get_rate(rates, original_currency, to):
    try:
        rate = [rate for origin, dest, rate in rates
                if (origin == original_currency and dest == to)][0]
        return rate
    except IndexError:
        print("Unsupported Currency")
        return 0


def same_rate(original_currency, to):
    if original_currency == to:
        return True
    else:
        return False


def convert(rates, value, original_currency, to):
    if same_rate(original_currency, to):
        return value
    return round(value * get_rate(rates, original_currency, to), 3)

if __name__ == '__main__':
    rates = [("USD", "EUR", 0.866),
             ("EUR", "USD", 1.154),
             ("EUR", "JPY", 0.007),
             ("JPY", "EUR", 137.20)]
    value = float(input("Please Enter a number: "))
    print("{} USD converts to {} EUR".format(round(value,3),convert(rates, value, "USD", "EUR")))
    print("{} USD converts to {} EUR".format(round(value,3),convert(rates, value, "EUR", "USD")))
    print("{} USD converts to {} EUR".format(round(value,3),convert(rates, value, "EUR", "JPY")))
    print("{} USD converts to {} EUR".format(round(value,3),convert(rates, value, "JPY", "EUR")))
