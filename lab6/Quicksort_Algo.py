def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers.copy()

    pivot = numbers[0]

    less = []
    equal = []
    greater = []

    for number in numbers:
        if number < pivot:
            less.append(number)
        elif number == pivot:
            equal.append(number)
        else:
            greater.append(number)

    return quick_sort(less) + equal + quick_sort(greater)