import re


def find_bigstate(given_data):

    usable_data = given_data[0].split(",")

    changed_data = []

    for string_to_search in usable_data:
        matches = re.finditer(r"\w+", string_to_search)
        transformed_data = [match.group(0) for match in matches]
        changed_data.append(transformed_data)

    data_list = []

    for i in range(len(changed_data)):
        data_list.append((changed_data[i][0], int(changed_data[i][2])))

    sum_of_city_population = {}  # Empty dictionary to find the big city

    for k, v in data_list:
        sum_of_city_population[k] = (
            v if k not in sum_of_city_population else sum_of_city_population[k] + v
        )

    return sum_of_city_population


print(
    find_bigstate(
        [
            "Kerala:A:2044040,Kerala:B:210120120,Kerala:C:3937238,Goa:A:22003993,Goa:B:2323"
        ]
    )
)
