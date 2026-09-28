import timeit

n = 100_000
big_list = list(range(n))
big_dict = {i: True for i in range(n)}   # dict comprehension, same idea as list comprehension

target = n - 1   # worst case: last item, forces a full scan of the list

list_time = timeit.timeit(lambda: target in big_list, number=100)
dict_time = timeit.timeit(lambda: target in big_dict, number=100)

print(f"list 'in' check (O(n)):  {list_time:.5f} sec for 100 lookups")
print(f"dict 'in' check (O(1)):  {dict_time:.5f} sec for 100 lookups")
print(f"list was {list_time / dict_time:.0f}x slower")
