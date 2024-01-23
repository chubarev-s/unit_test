
def compare_averages(list1, list2):
    avg_list1 = sum(list1) / len(list1)
    avg_list2 = sum(list2) / len(list2)

    print("-----------------------------------------")
    print("Среднее значение списка 1: ", avg_list1)
    print("Среднее значение списка 2: ", avg_list2)
    print("-----------------------------------------")

    if avg_list1 > avg_list2:
        print("Первый список имеет большее среднее значение")
        return "Первый список имеет большее среднее значение"
    elif avg_list1 < avg_list2:
        print("Второй список имеет большее среднее значение")
        return "Второй список имеет большее среднее значение"
    else:
        print("Средние значения равны")
        return "Средние значения равны"

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
compare_averages(list1, list2)