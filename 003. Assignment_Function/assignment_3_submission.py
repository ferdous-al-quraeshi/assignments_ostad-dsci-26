# Not mutating the original List
List = [1,5,2,9,3,22,13]

# function definition for ascending sort
def ascendingSort(list):
    sortedList = sorted(list)
    return sortedList

print("Unmutated Sort:", ascendingSort(List))
print("Original List:", List)

# ---------- #
# Mutating the original List

List = [1,5,2,9,3,22,13]

# function definition for ascending sort
def ascendingSort(list):
    list.sort()
    return list

print("Mutated Sort:", ascendingSort(List))
print("Original List got butated:", List)
