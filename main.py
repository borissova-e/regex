from pprint import pprint
import re

# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)


# TODO 1: выполните пункты 1-3 ДЗ
new_contacts_list = contacts_list
no_repetitions_list = []

# Пункт 1
for contact in new_contacts_list:
    contact_split = re.split(" ", contact[0])
    if len(contact_split) > 1:
        contact[0] = contact_split[0]
        contact[1] = contact_split[1]
        if len(contact_split) == 2:
            continue
        contact[2] = contact_split[2]
    else:
        contact_split_2 = re.split(" ", contact[1])
        if len(contact_split_2) == 2:
            contact[1] = contact_split_2[0]
            contact[2] = contact_split_2[1]

# Пункт 2
pattern = re.compile(r"(\+7|8)\s*\(?(\d+)[\)|-]?\s*(\d+)?[- ]?(\d+)?[- ]?(\d+)?")
pattern2 = re.compile(r"\s*\(?\доб\.?\s*(\d+)\)?")
for contact in new_contacts_list:
    contact[5] = pattern.sub(r"+7(\2)\3-\4-\5", contact[5])
    contact[5] = pattern2.sub(r" доб.\1", contact[5])

# Пункт 3
index_exeption = []
i = 0
j = 0
while i < len(new_contacts_list):
    if i in index_exeption:
        i += 1
        continue
    element = []
    j = i + 1
    while j < len(new_contacts_list):
        if new_contacts_list[i][0] == new_contacts_list[j][0]:
            if new_contacts_list[i][1] == new_contacts_list[j][1]:
                if (new_contacts_list[i][2] == new_contacts_list[j][2]) or (new_contacts_list[i][2] == '') or (
                        new_contacts_list[j][2] == ''):
                    index_exeption.append(j)
                    element.append(new_contacts_list[i][0])
                    element.append(new_contacts_list[i][1])
                    element.append(new_contacts_list[i][2])
                    x = 3
                    while x < len(new_contacts_list[i]):
                        element.append(new_contacts_list[i][x] + new_contacts_list[j][x])
                        x += 1
                    no_repetitions_list.append(element)
        j += 1
    if element == []:
        no_repetitions_list.append(new_contacts_list[i])
    i += 1

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(no_repetitions_list)
