## Binary Heap

A binary heap is a binary tree with following properties

- It is a complete tree (All levels are completly filled except the last level). This property makes them suitable to store in array
- It can be a min or max heap. In min heap the root node is small then all other and same applies to all other node further splited.'
- Practical use case of binary heap is Prim's algorithm, heap sort, priority queue
- The index of root node is always 1 and index of ledt child is calculated as 2*X and right child as 2*x + 1

**Types of Binary Heap**

1. Min Heap - Value of each node is less or equal to both of its children
2. Max Heap - Value of each node is greater or equal to both of its children

**Common operations performed on Binary Heap**

- creation of binary heap
- Peek top node
- Traverse
- Extract Min/Max
- size of binary heap
- Insert
- Deletion
