import random  # O(1) - Importing the random module for generating random numbers.

# A complete BST is a BST that is also a complete binary tree.
# After completing Task 1 above, extend your algorithm to complete the following task/s:
# Design an algorithm/method that, for a sequence of integers, re-orders the data items (i.e.,
# forms a new sequence) so that when the data items are inserted in order into an initially
# empty BST, the newly created BST will be a complete BST. Then re-do the same subtasks b)
# and c) as outlined in Task 1.
# For example, for an integer sequence of
# 45, -8, 21, 34, 55, 65, 9, 14, 0, 18, 90, 46, 49, 82, 84, 99, 80, 132, 57, 66
# your Task 1 may produce a balanced BST as shown in Figure 1 (a) or (b) (note that there can be many
# other balanced BSTs), but your Task 2 will only produce a tree shape as shown in Figure 1 (b). 

import random  # O(1) - Importing the random module for generating random numbers.

class Node:
    def __init__(self, Data):  # O(1) - Constructor for Node class.
        self.Data = Data  # O(1) - Assigns the data value to the node.
        self.Left = None  # O(1) - Initializes the left child node as None.
        self.Right = None  # O(1) - Initializes the right child node as None.

#Counting Sort
def CountingSort(Data):
    UnsortedArray = Data  # O(1) - Assigns the input array to UnsortedArray.
    FinalArray = [0] * len(UnsortedArray)  # Initialize FinalArray with zeros # O(n) - Creates an array of zeros with the same length as UnsortedArray.

    # Find the maximum and minimum elements in the array
    max_element = max(UnsortedArray)  # O(n) - Finds the maximum element in UnsortedArray.
    min_element = min(UnsortedArray)  # O(n) - Finds the minimum element in UnsortedArray.

    # Adjust the range to include negative numbers
    range_of_numbers = max_element - min_element + 1  # O(1) - Calculates the range of numbers in UnsortedArray.

    # Initialize count array with zeros
    count = [0] * range_of_numbers  # O(n) - Creates a count array initialized with zeros.

    # Count occurrences of each element
    for num in UnsortedArray:  # O(n) - Iterates through UnsortedArray.
        count[num - min_element] += 1  # O(1) - Increments the count of the corresponding element in the count array.

    # Update count array to contain actual positions of elements
    for i in range(1, len(count)):  # O(n) - Iterates through the count array.
        count[i] += count[i - 1]  # O(1) - Updates each element of the count array with cumulative counts.

    # Place elements in the sorted array
    for num in reversed(UnsortedArray):  # O(n) - Iterates through UnsortedArray in reverse.
        FinalArray[count[num - min_element] - 1] = num  # O(1) - Places each element in its correct position in the sorted array.
        count[num - min_element] -= 1  # O(1) - Decrements the count of the corresponding element in the count array.

    return FinalArray


def CreateBSTInput(SortedInput):
    if not SortedInput:  # O(1) - Checks if the input array is empty.
        return []

    MidPointIndex = len(SortedInput) // 2  # O(1) - Calculates the index of the midpoint.
    MidPoint = SortedInput[MidPointIndex]  # O(1) - Retrieves the value at the midpoint.
    LeftSubarray = SortedInput[:MidPointIndex]  # O(1) - Retrieves the left subarray.
    RightSubarray = SortedInput[MidPointIndex + 1:]  # O(1) - Retrieves the right subarray.

    return [MidPoint] + CreateBSTInput(LeftSubarray) + CreateBSTInput(RightSubarray)


def BuildBST(Data):
    if not Data:  # O(1) - Checks if the input data is empty.
        return None  # O(1) - Returns None if input data is empty.

    Nodes = [Node(D) for D in Data]  # O(n) - Creates node objects for each element in the input data.
    for Index, NodeValue in enumerate(Nodes):  # O(n) - Iterates through the nodes.
        LeftIndex = 2 * Index + 1  # O(1) - Calculates the index of the left child node.
        RightIndex = 2 * Index + 2  # O(1) - Calculates the index of the right child node.
        if LeftIndex < len(Nodes):  # O(1) - Checks if left child index is within bounds.
            NodeValue.Left = Nodes[LeftIndex]  # O(1) - Assigns the left child node.
        if RightIndex < len(Nodes):  # O(1) - Checks if right child index is within bounds.
            NodeValue.Right = Nodes[RightIndex]  # O(1) - Assigns the right child node.

    return Nodes[0]  # O(1) - Returns the root node of the BST.


def DisplayBST(Node, element="element", left="left", right="right"):
    def Display(root, element=element, left=left, right=right):
        if getattr(root, 'Right') is None and getattr(root, 'Left') is None:
            line = '%s' % root.Data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle  # O(1)

        if getattr(root, 'Right') is None:
            lines, n, p, x = Display(getattr(root, 'Left'))  # Recursion
            s = '%s' % root.Data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s  # O(n)
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '  # O(n)
            shifted_lines = [line + u * ' ' for line in lines]  # O(n)
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2  # O(n)

        if getattr(root, 'Left') is None:
            lines, n, p, x = Display(getattr(root, 'Right'))  # Recursion
            s = '%s' % root.Data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '  # O(n)
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '  # O(n)
            shifted_lines = [u * ' ' + line for line in lines]  # O(n)
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2  # O(n)

        left, n, p, x = Display(getattr(root, 'Left'))  # Recursion
        right, m, q, y = Display(getattr(root, 'Right'))  # Recursion
        s = '%s' % root.Data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '  # O(n)
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '  # O(n)
        if p < q:
            left += [n * ' '] * (q - p)  # O(n)
        elif q < p:
            right += [m * ' '] * (p - q)  # O(n)
        zipped_lines = zip(left, right)  # O(min(n, m))
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]  # O(n)
        return lines, n + m + u, max(p, q) + 2, n + u // 2  # O(n)

    lines = []
    if Node is not None:
        lines, *_ = Display(Node, element, left, right)  # O(n)
    print("\t== Binary Tree: shape ==")  # O(1)
    print()  # O(1)
    if lines == []:  # O(1)
        print("\t  No tree found")  # O(1)
    for line in lines:  # O(n)
        print("\t", line)  # O(1)
    print()  # O(1)

#Test 1
Input = [45, -8, 21, 34, 55, 65, 9, 14, 0, 18, 90, 46, 49, 82, 84, 99, 80, 132, 57, 66] # O(1) - Initializes an input array.

print("--------------------------------") # O(1) - Prints the spacer.
print("Original Data Sequence:") # O(1) - Prints the heading.
print(Input) # O(1) - Prints the input array.
SortedInput = CountingSort(Input) # O(1) - Sorts the input array.

print("\nSorted Data Items:") # O(1) - Prints the heading.
print(SortedInput)  # O(n*log(n)) - Prints the input sorted.
BSTInput = CreateBSTInput(SortedInput)

print("\nBST Input Data:") # O(1) - Prints the heading.
print(BSTInput)  # O(n*log(n)) - Prints the input data for the BST.
Root = BuildBST(BSTInput)

print("\nBST Tree Shape:") # O(1) - Prints the heading.
print("\n")
DisplayBST(Root)

#Test 2
NewInput = []

for Count in range(1,50):
    NewInput.append(random.randint(0, 100))

print("--------------------------------") # O(1) - Prints the spacer.
print("Original Data Sequence:") # O(1) - Prints the heading.
print(NewInput) # O(1) - Prints the newly generated input data.

print("\nSorted Data Items:") # O(1) - Prints the heading.
NewSortedInput = CountingSort(NewInput) # O(1) - Sorts the input array.
print(NewSortedInput)  # O(n*log(n)) - Prints the input sorted.

print("\nBST Input Data:") # O(1) - Prints the heading.
NewBSTInput = CreateBSTInput(NewSortedInput)
print(NewBSTInput)  # O(n*log(n)) - Prints the input data for the BST.

print("\nBST Tree Shape:") # O(1) - Prints the heading.
print("\n")
NewRoot = BuildBST(NewBSTInput)
DisplayBST(NewRoot)
print("--------------------------------") # O(1) - Prints the spacer.
