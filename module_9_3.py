first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


def difference_lengths():
    for a, b in zip(first, second):
        if len(a) != len(b):
            yield abs(len(a) - len(b))


def same_position_lengths():
    for i in range(min(len(first), len(second))):
        yield len(first[i]) == len(second[i])


first_result = list(difference_lengths())
second_result = list(same_position_lengths())

print(first_result)
print(second_result)