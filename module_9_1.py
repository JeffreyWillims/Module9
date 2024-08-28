# def min_func(lst):
#     return min(lst)
#
# def max_func(lst):
#     return max(lst)
#
# def len_func(lst):
#     return len(lst)
#
# def sum_func(lst):
#     return sum(lst)
#
# def sorted_func(lst):
#     return sorted(lst)
#
# def apply_all_func(int_list,  * functions):
#     results = {}
#     for func in functions:
#         results[func.__name__] = func(int_list)
#     return results
#
#
# print(apply_all_func([6, 20, 15, 9], max, min))
# print(apply_all_func([6, 20, 15, 9], len, sum, sorted))


def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))