def find_common_participants(first_group, second_group, sep = ','):
    participants_first = set(first_group.split(sep))
    participants_second = set(second_group.split(sep))
    common_participants = participants_first.intersection(participants_second)
    return list(common_participants)

first_group = "Иванов|Петров|Сидоров"
second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(first_group, second_group, sep = '|'))
