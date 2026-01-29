from Sorting_Algorithms.Insertion_Sort import InsertSort
from Sorting_Algorithms.Quick_sort import Quick
from BinarySearch import BinarySearch

Numb = [15, 4, 7, 8, 6, 0, 9, 11, 2, 26, 2, 5, 16, 1]

print(InsertSort(Numb))
print(Quick(Numb))

print(BinarySearch(Quick(Numb), 6))
print(BinarySearch(InsertSort(Numb), 6))