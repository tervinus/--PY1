import json


INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str) -> list[dict]:
    with open(filename) as f:
        csv_list = f.readlines() # поменял название переменной
    # передаю в список одну строку, в которой все содержимое файла
    csv_list = [lines.split() for lines in csv_list]  # убрал создание новой переменной под разделение списка
    # разделяю список на подсписки по символу конца строки
    changed_csv_list = []
    for buffer in csv_list:
        changed_csv_list += [lines.split(',') for lines in buffer]
    # тут я разделяю подсписки внутри на отдельные элементы по запятым
    # получается список списков, где элемент первого уровня строка, а второго - значение в ячейке в формате str
    # вот об этом месте я задавал вопрос
    headers_list = changed_csv_list[0]
    rows = changed_csv_list[1:]
    line_of_table = []
    for buffer in rows:  # исправил на передачу элемента, а не индекса
        dict_ = {headers_list[k]: buffer[k] for k in range(len(headers_list))}
        # использую вложенный цикл чтобы обращаться к элементам внутри подсписков
        line_of_table += [dict_]
    return line_of_table


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
