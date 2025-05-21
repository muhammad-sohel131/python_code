def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Even numbers count:", even_count)
    print("Odd numbers count:", odd_count)

numbers = [10, 21, 4, 45, 66, 93, 11]

count_even_odd(numbers)
