def compute_sum(a_list, n):
    # Check if the list is empty
    if len(a_list) == 0:
        return -1  # Return -1 for an empty list

    # Check if n is invalid
    if n <= 0 or n > len(a_list):
        return -1  # Return -1 for invalid n

    # Compute the sum of the first n elements using a loop
    sum_result = sum(a_list[:n])

    return sum_result


def compute_avg(a_list, n):
    sum_result = compute_sum(a_list, n)

    if sum_result == -1:
        return -1
    else:
        avg_result = sum_result / n
        return avg_result


a_list = [10, 9, 8, 7, 6]
print(compute_avg(a_list, 4))


def main():
    # Test case 1
    assert compute_sum([1, 2, 3, 4], 4) == 10
    assert compute_avg([1, 2, 3, 4], 4) == 2.5

    # Test case 2
    assert compute_sum([1, 2, 3, 4], 3) == 6
    assert compute_avg([1, 2, 3, 4], 3) == 2.0

    # Test case 3
    assert compute_sum([], 2) == -1
    assert compute_avg([], 2) == -1


main()
