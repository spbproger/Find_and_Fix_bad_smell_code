# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    data = _read_data(csv)
    data = sort_by_age(data)
    return filter_by_age(data)


def _read_data(csv):
    return [line.split(';') for line in csv.split('\n')]


def sort_by_age(data):
    return sorted(data, key=lambda x: int(x[1]))


def filter_by_age(data):
    return list(filter(lambda x: int(x[1]) >= 10, data))


if __name__ == '__main__':
    print(get_users_list())
