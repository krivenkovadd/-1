def find_common_participants(participants_first_group, participants_second_group, sep = ','):
    participants_first = set(participants_first_group.split(sep))
    participants_second = set(participants_second_group.split(sep))
    common_participants = participants_first.intersection(participants_second)
    return list(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group,participants_second_group, sep = '|'))