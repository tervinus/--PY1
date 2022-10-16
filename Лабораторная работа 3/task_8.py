money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
delta = spend - salary
while delta < money_capital:
    month += 1
    spend *= 1+increase
    money_capital -= delta
    delta = round(spend - salary, 2)
print(month)
