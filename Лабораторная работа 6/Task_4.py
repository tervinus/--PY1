import json


INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str) -> list[dict]:
    with open(filename) as f:
        csv_text = f.readlines()
    csv_list = [lines.split() for lines in csv_text]
    changed_csv_list = []
    for i in range(len(csv_list)):
        buffer = csv_list[i]
        changed_csv_list += [lines.split(',') for lines in buffer]
    headers_list = changed_csv_list[0]
    rows = changed_csv_list[1:]
    line_of_table = []
    for i in range(len(rows)):
        buffer = rows[i]
        dict_ = {headers_list[k]: buffer[k] for k in range(len(headers_list))}
        line_of_table += [dict_]
    return line_of_table




print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
