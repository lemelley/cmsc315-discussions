"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # insert() puts the value at the index and shifts every element after it one spot to the right
    # Inserting at the end doesn't require any shifting (fastest)
    # Inserting at the beginning forces everything to shift (slowest)
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Check the index first so a bad index returns "None" instead of crashing with an IndexError
    if 0 <= index < len(lst):
        # pop() removes the value and shifts every element after it one spot to the left
        return lst.pop(index)
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Using a linear search here to check each element in order, starting at the first, until a match is found
    # The list is not sorted so the program needs to go through every element
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== Insertion Tests ===")
    numbers = [10, 20, 30, 40, 50]
    print("Original list:", numbers)
    insert_at(numbers, 0, 5)
    print("Inserted 5 at the beginning:", numbers)
    insert_at(numbers, 3, 25)
    print("Inserted 25 in the middle (index 3):", numbers)
    insert_at(numbers, len(numbers), 60)
    print("Inserted 60 at the end:", numbers)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== Deletion Tests ===")
    print("Removed from the beginning:", delete_at(numbers, 0), "->", numbers)
    print("Removed from the middle (index 3):", delete_at(numbers, 3), "->", numbers)
    print("Removed from the end:", delete_at(numbers, len(numbers) - 1), "->", numbers)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== Search Tests ===")
    print("Searching for 40 (exists): found at index", search_value(numbers, 40))
    print("Searching for 99 (missing): returned", search_value(numbers, 99))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== Edge Cases ===")
    print("Delete using an invalid index (50):", delete_at(numbers, 50))
    empty = []
    print("Delete from an empty list:", delete_at(empty, 0))
    insert_at(empty, 0, 7)
    print("7 Inserted into an empty list:", empty)

    # Real-world scenario: a music playlist
    print("\n=== REAL-WORLD SCENARIO: PLAYLIST ===")
    playlist = ["Hey Jude", "Yesterday", "Yellow Submarine"]
    print("Playlist:", playlist)
    insert_at(playlist, 1, "Eleanor Rigby")
    print("Added Eleanor Rigby as the second track:", playlist)
    print("Removed:", delete_at(playlist, 0), "->", playlist)
    print("Yellow Submarine is track number", search_value(playlist, "Yellow Submarine") + 1)


if __name__ == "__main__":
    main()