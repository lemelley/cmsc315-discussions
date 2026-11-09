"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # When insert is called, the method calls on _insert_recursive to place the values in their correct spot.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # if the node is empty, a new node is created with the entered value
        if node is None:
            return Node(value)
        # smaller values are inserted to the left and larger values to the right which keeps the tree in order
        # because of this, searching and traversal function:
        # if the inserted value is less than the current node value, the value is inserted to the left
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        # if the inserted value is greater than the current node value, the value is inserted to the right
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # once the insertions are completed, the current node is returned so the parent keeps its links
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST search is more efficient because each comparison lets the program skip one side of the tree
        # given a tree that is balanced, it takes significantly less steps than going through every value.
        # Although this is usually faster, the advantage is lost if the tree is lopsided such as when values are inserted
        # in sorted order because then it can take as many steps as a linear search would.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # When reaching the end of a branch, False is returned because the Node is empty
        if node is None:
            return False
        # If the value in the current node is found, True is returned
        if value == node.value:
            return True
        # If the value is less than that of the current value, the recursion continues to the left of the tree
        if value < node.value:
            return self._search_recursive(node.left, value)
        # If none of other conditions are true, the recursion continues to the right
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # In order traversal goes to the left subtree, then the current node, then the right subtree
        # The left side holds the smaller values and the right side holds the larger values
        # Going in that order sorts the values from smallest to largest
        if node is not None:
            # First, the program goes to everything in the left subtree (everything smaller)
            self._inorder_recursive(node.left, values)
            # Then, the current nodes value is recorded
            values.append(node.value)
            # Lastly, the program goes to everything in the right subtree (everything larger)
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.
    # Values go into both the left and right subtrees
    tree = BST()
    # Values smaller than 40 go in the left and larger go to the right
    # A BST is efficient because each comparison skips one side of the tree which reduces the area needing to be searched
    values = [40, 30, 90, 50, 20, 70, 10]
    for value in values:
        tree.insert(value)
    print("Inserted values in this order:", values)

    print("\n=== IN-ORDER TRAVERSAL ===")
    # The traversal prints sorted output even though the values were inserted out of order because the left side
    # is always going to be the smaller side and the right side the larger
    print("Traversal results: ", tree.inorder())
    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    # 20 and 70 are in the tree so they both return True.
    # 100 and 45 are not, so the search runs off the corresponding ends of the tree and returns False
    print("Search 20 (exists):", tree.search(20))
    print("Search 70 (exists):", tree.search(70))
    print("Search 100 (missing):", tree.search(100))
    print("Search 45 (missing):", tree.search(45))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    # Edge Case 1: an empty tree has no nodes so traversal returns an empty list and a search returns False
    empty_tree = BST()
    print("Traversing an empty tree:", empty_tree.inorder())
    print("Searching an empty tree:", empty_tree.search(10))

    # Edge case 2: 50 is already in the tree, so a duplicate is ignored and the traversal isn't affected
    tree.insert(50)
    print("After inserting duplicate number (50):", tree.inorder())

    # Edge case 3: a tree with a single node is just the root, so the traversal returns the single value.
    one_node = BST()
    one_node.insert(5)
    print("Tree with only one node:", one_node.inorder())

    # Real-world scenario: leaderboard of hours calibrated in the past week (Real data, names changed)
    print("\n=== REAL-WORLD SCENARIO: CAL HOUR LEADERBOARD ===")
    leaderboard = BST()
    entries = [(37, "Mason"), (32, "Colin"), (30, "Gage"), (25, "Gunar"), (18, "Ryan"), (14, "Irvin"), (8, "Eligh")]
    for hours, name in entries:
        leaderboard.insert((hours, name))
    # In order, gives lowest to highest hours, so reversed() puts the top hours first
    print("Calibration Hours Leaderboard:")
    for hours, name in reversed(leaderboard.inorder()):
        print(f" {name}: {hours} hours")

    print("Is Irvin with 14 hours on the leaderboard?", leaderboard.search((14, "Irvin")))
    print("Is Richard with 2 hours on the leaderboard?", leaderboard.search((2, "Richard")))

if __name__ == "__main__":
    main()