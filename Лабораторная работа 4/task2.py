def get_count_char(str_):
    letters_dict = {}
    sep_string = str_.split()
    united_string = ''.join(sep_string)
    united_string = united_string.lower()
    for char in united_string:
        if char.isalpha():
            if char in letters_dict:
                letters_dict[char] += 1
            else:
                letters_dict[char] = 1
    return letters_dict


def get_percent_char (dict_): # Это вторая функция из пункта 5, которая выводит процент данного символа
    percent_dict = {}
    total_sum = sum(dict_.values())
    for char, count in dict_.items():
        percent_dict[char] = round(count/total_sum, 2)
    return percent_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
# print(get_percent_char(get_count_char(main_str)))
# я закоментировал данную строку с выводом результата второй функции чтобы можно было пройти проверку
