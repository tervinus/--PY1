salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
need_money += spend-salary
for _ in range(months-1):
    spend *= 1+increase
    need_money += spend-salary
print(round(need_money))
