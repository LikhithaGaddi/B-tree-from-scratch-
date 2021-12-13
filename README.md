## Commands:

- To execute the python file:

  > python3 2020201066_Assignment3.py <input_file>

## Insert :

- First search for the node
- If the value already exists, then increase the count
- If not, then traverse the tree and get the node where we have to insert
- Insert the value and check if there is overflow
- If there is no overflow, then return
- If there is then handling this is different for leaf node and non-leaf node: - For leaf node :- Split the data into two nodes. Middle value(right biased) will be the value which is going to the root. Here right node contains the value which is going to root. Also spli the respective pointers - For non-leaf node :- Split the data into two nodes. Middle value(right biased) will be the value which is going to the root. Here right node doesn't contains the value which is going to root. Also spli the respective pointers
- If there is overflow send the references of the two nodes and the value that needs to be included in the root to the parent of the present node.
- Repeat the process till the root node.

## Range :

- Search for the node which contains first value between the given range.
- The one advantage of the B+ tree is leaf nodes are connect.
- Here we can traverse the leaf nodes till there is value which exceed the given range is encountered
- While doing this count the occurances of each of the key value
- Return the count

## Count:

- Search for the node which contains the value
- Return the count of the value if peresnt in tree, else return 0

## Find:

- Search for the value in the tree using pointers of the node
- If the value if present then return YES
- Else return NO

## Input and Output Format:

- Input should be a .txt file containing any of the below queries: - INSERT <key> - FIND <key> - COUNT <key> - Range <key,key>
- Input filename should be passed as a command line argument
- Output for the queries will be written into a file names "output.txt" and also printed on the console
- The spacing between the queires should be exactly as mentioned in the above

## Constraints:

- Input keys should be integers as mentioned in the assignment
