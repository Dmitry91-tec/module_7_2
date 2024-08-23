import io
from pprint import pprint
def custom_write(file_name, strings):
    f = open(file_name, 'w', encoding = 'utf-8')
    for index in strings:
        f.write(index+'\n')
    f.close()
    with open(file_name,'r', encoding='utf-8') as f:
        dict_result ={}
        strings_ = f.read().count('\n')
        f.seek(0)
        for line_number in range(strings_):
            dict_result.update({(line_number+1, f.tell()): f.readline()})
            line_number +=1

    return dict_result

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)