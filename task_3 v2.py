OUTPUT_FILE = "output.csv"


def prepare_line(list_: list, delimiter: str, new_line: str):
    for i in range(len(list_)):
        if i == len(list_)-1:
            list_[i] += new_line
        else:
            list_[i] += delimiter
# Эта функция нужна чтобы расставить разделители для разделения столбцов
# и поставить последнему элементу символ конца строки


def to_csv_file(filename: str, headers: list, rows: list, delimiter: str = ',', new_line: str = '\n'):
    headersc = headers.copy()
    rowsc = rows.copy()
    # тут я применяю копирование, чтобы не поменять входные данные, так как листы предаются по ссылке
    prepare_line(headersc, delimiter, new_line)
    for buffer in rowsc:  # исправил замечание, теперь педедаю элемент, а не индекс.
        prepare_line(buffer, delimiter, new_line)
    buffer_list = [headersc, *rowsc]
   # создаю список списков, где каждый элемент - строка таблицы.
    table_list = []
    for item in buffer_list:   # тут тоже исправил
        table_list += [*item]
    # превращаю список списков в список строк для построчной записи.
    # Как распаковать сразу не придумал, работало только так)
    with open(filename, 'w') as f:
        f.writelines(table_list)


headers_list = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']
data = [
    ['-122.050000', '37.370000', '27.000000', '3885.000000', '661.000000', '1537.000000', '606.000000', '6.608500', '344700.000000'],
    ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000', '809.000000', '277.000000', '3.599000', '176500.000000'],
    ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000', '1484.000000', '495.000000', '5.793400', '270500.000000'],
    ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000', '49.000000', '11.000000', '6.135900', '330000.000000'],
]

to_csv_file(OUTPUT_FILE, headers_list, data)

with open(OUTPUT_FILE) as output_f:
    for line in output_f:
        print(line, end="")
