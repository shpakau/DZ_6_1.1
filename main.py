# Дан список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух
# целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"',
# 'градусов']

# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!

input_list = ['в', '5', 'часов', '17', 'минут',
              'температура', 'воздуха', 'была', '+5', 'градусов']
length_of_list: int = len(input_list)
store_id = id(input_list)

for _ in range(length_of_list):

    elem = input_list.pop(0)

    if  elem.isdigit() and elem.isalnum():
        input_list.append(f'"{int(elem):02d}"')
    elif elem[0] == "+" and elem[1].isdigit():
        input_list.append(f'"+{int(elem):02d}"')
    else:
        input_list.append(elem)

print(' '.join(input_list))