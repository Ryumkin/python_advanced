def calculate_original_index_of_taxi_fare():
    result_index_list = list(map(get_original_index,
                                 list_of_employees_total_home_distance_in_km))
    print(*result_index_list, sep=" ")


def get_original_index(employees_total_home_distance_in_km):
    return list_of_tax_fare_per_km.index(
        zipped_dictionary[employees_total_home_distance_in_km])


def collect_data():
    global sorted_list_of_employees_total_home_distance_in_km, \
        sorted_list_of_taxi_fares_per_km, \
        list_of_tax_fare_per_km,\
        list_of_employees_total_home_distance_in_km,\
        zipped_dictionary
    user_input1 = input()
    user_input2 = input()
    list_of_employees_total_home_distance_in_km = list(
        map(int, user_input1.split()))
    sorted_list_of_employees_total_home_distance_in_km = sorted(
        list_of_employees_total_home_distance_in_km, reverse=True)
    list_of_tax_fare_per_km = list(map(int, user_input2.split()))
    sorted_list_of_taxi_fares_per_km = sorted(list_of_tax_fare_per_km)
    zipped_dictionary = dict(
        zip(sorted_list_of_employees_total_home_distance_in_km,
            sorted_list_of_taxi_fares_per_km))
    calculate_original_index_of_taxi_fare()


collect_data()

"""print(
    *map(
        lambda x: x[1][0],
        sorted(
            zip(
                sorted(
                    enumerate(map(int, input().split())),
                    key=lambda x: x[1]
                ),
                sorted(
                    enumerate(map(int, input().split())),
                    key=lambda x: x[1],
                    reverse=True
                )
            ),
            key=lambda x: x[0][0]
        )
    )
)
"""

"""people = map(int, input().split())
sorted_people = sorted(enumerate(people), key=lambda x: x[1])
taxi = map(int, input().split())
sorted_taxi = sorted(enumerate(taxi), key=lambda x: x[1], reverse=True)
ans = zip(sorted_people, sorted_taxi)
sorted_ans = sorted(ans, key=lambda x: x[0][0])
print(*map(lambda x: x[1][0], sorted_ans))
"""
