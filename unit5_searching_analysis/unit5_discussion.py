"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # for loop is utilized to search through the list for the entirety of the range
    # A linear search has O(n) time complexity because in the worst case scenario, it goes through an entire list
    # looking for the desired item. The longer the list, the longer time it takes to search through the list
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Given a sorted list, binary can be quicker for larger lists because it cuts the search area in half every time
    # it goes looking for the target item
    # low is set to the lowest part of the list
    low = 0
    # high is set to the last value in the range
    high = len(lst) - 1
    # while loop is utilized so that the program keeps searching for the given item until it is found
    while low <= high:
        # mid is established by dividing the range of the list in half
        mid = (low + high) // 2
        # the program checks if mid is the target
        if lst[mid] == target:
            # mid is returned if it is the target
            return mid
        # if the mid value is less than the target, the search area is narrowed to the upper half of the range
        elif lst[mid] < target:
            # the value above mid (because mid was checked) is set as the new low which cuts the search area in half
            low = mid + 1
        # if the mid value is greater than the target, the search area is narrowed to the bottom half of the range
        else:
            # the value below mid (because mid was checked) is set as the new high which cuts the search area in half
            high = mid - 1
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    small = [4, 9, 17, 24, 41, 59, 73]
    print("Dataset:", small)

    print("Searching for a value that exists")
    print("Linear search for 24:", linear_search(small, 24))
    print("Binary search for 24:", binary_search(small, 24))

    print("Searching for a value that does not exist")
    print("Linear search for 60:", linear_search(small, 60))
    print("Binary search for 60:", binary_search(small, 60))
    # Both searches found 24 at index 3 and returned -1 for 60, so they give the same result. There are only 7 items in
    # the list so the time difference is negligible

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    large = list(range(0, 2000000))
    target = 1999999 # target is set to the last item in the list, worst case scenario for linear search

    print("The Dataset size is:", len(large))
    print("Linear search found index:", linear_search(large, target))
    print("Binary search found index:", binary_search(large, target))

    # A linear search checks each item in the list so in the worst case, it goes through the entire range of the list
    print("Worst case for linear search:", len(large), "checks were conducted for this example")

    # Binary search cuts the search area in half each step, so the following counts how many halves are conducted
    halves = 0
    size = len(large)
    while size > 1:
        size = size // 2
        halves += 1
    print("Worst case for binary search:", halves, "times that the list was halved for this example")
    # Linear needs 2,000,000 checks to find the target whereas the binary search only needs 20. Doubling the size of the
    # list would double the steps needed for a linear search, but only one more step for a binary search.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # Empty list: nothing to search for
    # Both return -1. The linear search loop has nothing to go through and the binary high starts at -1 so the while
    # loop never runs
    empty = []
    print("Given an empty list, linear search for 5:", linear_search(empty, 5))
    print("Given an empty list, binary search for 5:", binary_search(empty, 5))

    # Single-element list. One instance where the value exists
    # Both return index 0 since there is only one item to check
    single = [9]
    print("Given a list with one value [9]:")
    print("Linear search for [9] shows:", linear_search(single, 9))
    print("Binary search for [9] shows:", binary_search(single, 9))

    # Single-element list. One instance where the value does not exist
    # Both searches return -1 since the target is not in the list
    print("Given a list with one value [9]:")
    print("Linear search for [12] shows:", linear_search(single, 12))
    print("Binary search for [12] shows:", binary_search(single, 12))

    # Value search for first position of a list:
    edge = [2, 6, 9, 16, 19, 21]
    print("Given a list of values:")
    # Linear search finds the first item instantly since it starts at the beginning of the list, but has to go through
    # the entire range for the last one. In comparison, a binary search finds either end of the list in a couple of steps
    print("First item in the list search for [2] shows:", linear_search(edge, 2), "For linear search, and",
          binary_search(edge, 2), "For a binary search")
    # Value search for the last position of a list:
    print("Last item in the list search for [21] shows:", linear_search(edge, 21), "For linear search, and",
          binary_search(edge, 21), "For a binary search")

    print("\n=== REAL-WORLD SCENARIO: CALIBRATION RECORDS ===")

    # The database is sorted by equipment serial number, so binary search works well here
    serial_numbers = [115004, 116234, 116526, 119427, 124398, 127438, 127561, 147622, 184386]
    print("Sorted asset serial numbers:", serial_numbers)
    # A binary search is conducted on the sorted list which returns the index of the serial number being searched for
    print("Binary search for SN: 127438 (in the records):", binary_search(serial_numbers, 127438))
    # Another binary search is conducted for a serial number not in the list, returns -1 since the item's not in the list
    print("Binary search for SN: 116528 (not in the records):", binary_search(serial_numbers, 116528))

    # The list of SN's that will get worked on today are in no specific order:
    workload_numbers = [127561, 116526, 115004, 184386]
    print("Today's planned workload serial numbers:", workload_numbers)
    # Linear search works best here because the items in the list are not sorted
    print("Linear search for SN 116526:", linear_search(workload_numbers,116526))

    # Binary search on an unsorted list gives the wrong answer, so it can't be used here
    print("Binary search for 127561 in the unsorted list:", binary_search(workload_numbers, 127561))
    print("Linear search for 127561 in the unsorted list:", linear_search(workload_numbers, 127561))

if __name__ == "__main__":
    main()