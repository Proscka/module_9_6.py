def all_variants(text):
    a = len(text)
    for length in range(1,a + 1):
        for start in range(a - length + 1):
            yield text[start:start + length]


a = all_variants("abc")
for i in a:
    print(i)