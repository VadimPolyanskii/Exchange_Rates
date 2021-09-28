from forex_python.converter import CurrencyRates

# Курс доллара к рублю
c = CurrencyRates()
print(c.get_rate('USD', 'RUB'))

