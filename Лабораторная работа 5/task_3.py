from random import randint


def get_unique_list_numbers() -> list[int]:
    list_numbers = [1]
    while len(list_numbers) < 15:
        candidate = randint(-10, 10)
        i = 0
        for number in list_numbers:
            if candidate == number:
                 i += 1
        if i == 0 :
            list_numbers.append(candidate)
    return list_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
