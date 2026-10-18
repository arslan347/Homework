usd_to_rubles= 95.50
def convert_usd_to_rub(amount_usd):
    return amount_usd * usd_to_rubles
dollars = float(input("Введите сумму в долларах: "))
rubles = convert_usd_to_rub(dollars)
print(f"{dollars:.2f} USD = {rubles:.2f} RUB")
