import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Считываем содержимое CSV файла
    with open(INPUT_FILENAME, 'r') as input_file:
        reader = csv.DictReader(input_file)
        data = list(reader)

    # Сериализуем данные в JSON формат с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as output_file:
        json.dump(data, output_file, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

