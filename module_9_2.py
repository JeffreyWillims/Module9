first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = list(map(len, filter(lambda s: len(s) >= 5, first_strings)))


second_result = []
for word1 in first_strings:
    for word2 in second_strings:
        if len(word1) == len(word2):
            second_result.append((word1, word2))


third_result = {}
for word in first_strings + second_strings:
    if len(word) % 2 == 0:
        third_result[word] = len(word)

print(first_result)
print(second_result)
print(third_result)