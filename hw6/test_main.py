import pytest


from hw6.main import compare_averages

def test_compare_averages_greater():
    list1 = [10, 20, 30, 40, 50]
    list2 = [1, 2, 3, 4, 5]
    assert compare_averages(list1, list2) == "Первый список имеет большее среднее значение"

def test_compare_averages_lesser():
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40, 50]
    assert compare_averages(list1, list2) == "Второй список имеет большее среднее значение"

def test_compare_averages_equal():
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 5]
    assert compare_averages(list1, list2) == "Средние значения равны"
