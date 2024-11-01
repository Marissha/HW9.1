def apply_all_func(int_list, *functions):
    results = dict()
    for i in range(len(functions)):
        results[f'{functions[i].__name__}'] = f'{functions[i](int_list)}'
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
