def selection_sort(xs):
    min_index = 0
    min_value = xs[0]
    while min_index<len(xs)-1:
        for i in range(min_index,len(xs)):
            if xs[i] < xs[min_index]:
                temp = xs[min_index]
                xs[min_index] = xs[i]
                xs[i] = temp
        min_index += 1
    return xs

        


xs = [3, 2, 1, 5, 4]
print(xs)
selection_sort(xs)
print(xs)

# A nice Pythonic way to check  a list is sorted
# without relying on using Python's own sorting methods to compare.
print(all(xs[i] <= xs[i + 1] for i in range(len(xs) - 1)))
