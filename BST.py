
class Node:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def findMin_ini(self):
        FNode = self.findMin(self.root)
        return FNode

    def findMax_ini(self):
        FNode = self.findMax(self.root)
        return FNode

    def traverseInOrder_ini(self):
        self.traverseInOrder(self.root)

    def findMin(self, root):
        x = root  # Start at the root
        while x.left != None:  # Continue left until we find the min value
            x = x.left
        return x

    def findMax(self, root):
        x = root  # Start at the root
        while x.right != None:  # Continue right to find max value
            x = x.right
        return x

    def insert(self, key):
        self.root = self.insertInTree(self.root, key)

    def insertInTree(self, root, key):
        trail = None  # Trailing pointer for x
        new = Node(key)  # Create a new node for the key we are inserting
        x = root  # Start traversing from the root, downward to find a place of insertion for the new node
        while x != None:  # Until we reach a None value
            trail = x
            if new.key < x.key:  # If the key we are inserting is less than the key we are currently at, continue left
                x = x.left
            else:  # If the key we are inserting is greater than or equal the key we are currently at, continue right
                x = x.right
        if trail == None:  # if the root is None/tree is empty, then new node becomes the root
            root = new
        elif new.key < trail.key:  # New node becomes left child if the new node key is < than leaf key
            trail.left = new
        else:  # Else, the new node becomes the right child
            trail.right = new
        return root

    def delete(self, root, key):
        if root == None:  # If tree is empty, return None
            return root
        if key < root.key:  # Key is in left subtree
            root.left = self.delete(root.left, key)
        elif key > root.key:  # Key is in right subtree
            root.right = self.delete(root.right, key)
        else:  # Key is found, must now delete
            # Case 1: No child exists
            if root.left == None:
                x = root.right
                root = None  # Replace root with
                return x
        # Case 2: 1 child exists
            elif root.right == None:
                x = root.left
                root = None
                return x
        # Case 3: 2 children exist
        # Get the smallest key in the right subtree (the inorder successor)
            x = self.findMin(root.right)
            # Store inorder successor to the root node
            root.key = x.key
            # Delete inorder successor
            root.right = self.delete(root.right, x.key)
        return root

    def traverseInOrder(self, root):
        if root:  # Inorder traversal
            self.traverseInOrder(root.left)
            print(root.key, end=" ")
            self.traverseInOrder(root.right)

    def traverseInOrder_ini(self):
        self.traverseInOrder(self.root)
        print()

    def traversePreOrder(self, root):
        if root:
            print(root.key, end=" ")
            self.traversePreOrder(root.left)
            self.traversePreOrder(root.right)

    def traversePreOrder_ini(self):
        self.traversePreOrder(self.root)
        print()

    def traversePostOrder(self, root):
        if root:
            self.traversePostOrder(root.left)
            self.traversePostOrder(root.right)
            print(root.key, end=" ")

    def traversePostOrder_ini(self):
        self.traversePostOrder(self.root)
        print()

    def delete_ini(self, key):
        # Updates the new root after running through deletion function
        self.root = self.delete(self.root, key)

    def getRoot(self):
        return self.root


def main():
    Tree = BST()
    print("\n------------ BST - Priority Queue ------------")
    insert = True
    while (True):
        if insert:
            print(
                "\nEnter an INTEGER into the BST.\nEnter \"f\" or \"F\" to finish.\n")
            choice = validate()
            if choice not in (["f", "F"]):
                Tree.insert(choice)
                continue
        print("\n1. Insert more values\n2. Delete\n3. Find Max\n4. Find Min\n5. Find Root",
              "\n6. In-order Traversal\n7. Pre-order Traversal\n8. Post-order Traversal\nF. Quit\n")
        choice = validate()
        print()
        if choice == 1:
            insert = True
            continue
        elif choice == 2:
            print("Enter a value to delete")
            Tree.delete_ini(validate())
        elif choice == 3:
            print("Max Value: ", Tree.findMax_ini().key)
        elif choice == 4:
            print("Min Value: ", Tree.findMin_ini().key)
        elif choice == 5:
            print(Tree.getRoot().key)
        elif choice == 6:
            print("In-order Traversal:")
            Tree.traverseInOrder_ini()
        elif choice == 7:
            print("Pre-order Traversal:")
            Tree.traversePreOrder_ini()
        elif choice == 8:
            print("Post-order Traversal:")
            Tree.traversePostOrder_ini()
        elif choice in ["f", "F"]:
            break
        insert = False


def validate():
    while True:
        try:
            choice = input("Please enter a valid choice: ")
            if choice in (["f", "F"]):
                return choice
            return int(choice)
        except ValueError:
            print("That was not a valid choice...\n")


if __name__ == "__main__":
    main()
