#!/usr/bin/env python


def add(numbers):
    if not numbers:
        return 0
    delimiter = ','
    if numbers.startswith('//'):
        delimiter, numbers = numbers.split('\n', 1)
        delimiter = delimiter[2:]
    numbers = numbers.replace("\n", delimiter)
    return sum(map(int, numbers.split(delimiter)))

if __name__ == '__main__':
    assert add("") == 0
    assert add("1") == 1
    assert add("1,2") == 3
    assert add("1,2,3") == 6
    assert add("1\n2,3") == 6
    assert add("//;\n1;2") == 3