# TODO решите задачу
import json
def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    total_sum = 0
    for item in data:
        score = item['score']
        weight = item['weight']
        product = score * weight
        total_sum += product

    return round(total_sum, 3)


print(task())
