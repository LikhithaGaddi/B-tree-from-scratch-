import sys
import os


class Node:
    def __init__(self, order):
        self.max_keys = order - 1
        self.keys = []
        self.pointers = []
        self.counts = {}
        self.parent = None
        self.isLeaf = False


class BPlusTree:
    def __init__(self, order):
        self.root = None
        self.order = order
        self.max_keys = order-1

    def __insert_at_index__(self, l, value):
        index = 0
        if (l[0] > value):
            l.insert(index, value)
            return l
        index = len(l)
        for i in range(0, len(l)):
            if (value < l[i]):
                index = i
                break

        l.insert(index, value)
        return l

    def __get_index__(self, l, value):
        index = 0
        for i in range(0, len(l)):
            if (value <= l[i]):
                index = i
                break
        return index

    def __getNode__(self, val):
        curr_node = self.root
        while (curr_node.isLeaf != True):
            temp = curr_node.keys
            for i in range(0, len(temp)):
                if (i == 0 and val < temp[i]):
                    curr_node = curr_node.pointers[i]
                    break
                elif (i == len(temp) - 1 and val >= temp[i]):
                    curr_node = curr_node.pointers[i + 1]
                    break
                elif (val < temp[i] and val >= temp[i - 1]):
                    curr_node = curr_node.pointers[i]
                    break

        return curr_node

    def find(self, val):
        if self.root == None:
            return "NO"
        node = self.__getNode__(val)
        for i in range(len(node.keys)):
            if (node.keys[i] == val):
                return "YES"
        return "NO"

    def search(self, val):
        if self.root == None:
            return False
        node = self.__getNode__(val)
        flag = False
        for i in range(len(node.keys)):
            if (node.keys[i] == val):
                node.counts[val] += 1
                flag = True
                break
        return flag

    def count(self, val):
        if self.root == None:
            return 0
        node = self.__getNode__(val)
        for i in range(len(node.keys)):
            if (node.keys[i] == val):
                return node.counts[val]
        return 0

    def range(self, x, y):
        if self.root == None:
            return 0
        node = self.__getNode__(x)
        count = 0
        while (1):
            for i in range(0, len(node.keys)):
                if (node.keys[i] >= x and node.keys[i] <= y):
                    count += node.counts[node.keys[i]]
                if (node.keys[i] > y):
                    break
            if (len(node.pointers) == 0):
                break
            node = node.pointers[0]
        return count

    def split(self, val, node):
        if (node.isLeaf):
            m = len(node.keys)
            node.keys = self.__insert_at_index__(node.keys, val)
            if(len(node.keys) > self.max_keys and not node == self.root):
                value = node.keys[m // 2]
                temp_node = Node(self.order)
                temp_node.counts = node.counts
                temp_node.counts[val] = 1
                temp_node.keys = node.keys[m // 2:]
                temp_node.pointers = node.pointers
                node.keys = node.keys[:m // 2]
                node.pointers = [temp_node]
                node.isLeaf = True
                temp_node.isLeaf = True
                return [value, node, temp_node]
            elif (len(node.keys) > self.max_keys and node == self.root):
                value = node.keys[m // 2]

                temp_node = Node(self.order)
                temp_node.counts = node.counts
                temp_node.counts[val] = 1
                temp_node.keys = node.keys[m // 2:]
                temp_node.pointers = node.pointers
                node.keys = node.keys[:m // 2]
                node.pointers = [temp_node]
                node.isLeaf = True
                temp_node.isLeaf = True

                s_node = Node(self.order)
                s_node.keys.append(value)
                s_node.counts[value] = 1
                s_node.pointers.append(node)
                s_node.pointers.append(temp_node)
                self.root = s_node
                return [None, None, None]
            else:
                node.counts[val] = 1
                return [None, None, None]
        else:
            temp = node.keys
            for i in range(0, len(temp)):
                if (i == 0 and val < temp[i]):
                    c_node = node.pointers[i]
                    break
                elif (i == len(temp) - 1 and val >= temp[i]):
                    c_node = node.pointers[i + 1]
                    break
                elif (val < temp[i] and val >= temp[i - 1]):
                    c_node = node.pointers[i]
                    break
            temp = self.split(val, c_node)

            if temp[0] == None:
                return [None, None, None]
            else:
                val = temp[0]
                node.keys = self.__insert_at_index__(node.keys, val)
                val_index = self.__get_index__(node.keys, val)
                if (len(node.keys) > self.max_keys and not node == self.root):
                    index = self.__get_index__(node.keys, val)
                    node.pointers[index] = temp[1]
                    node.pointers.insert(index + 1, temp[2])
                    m = len(node.keys)
                    value = node.keys[m//2]
                    temp_node = Node(self.order)
                    temp_node.keys = node.keys[m // 2 + 1:]
                    temp_node.counts = node.counts
                    temp_node.pointers = node.pointers[m // 2 + 1:]
                    node.keys = node.keys[:m // 2]
                    node.pointers = node.pointers[:m // 2 + 1]
                    return [value, node, temp_node]

                elif (len(node.keys) > self.max_keys and node == self.root):
                    index = self.__get_index__(node.keys, val)
                    node.pointers[index] = temp[1]
                    node.pointers.insert(index + 1, temp[2])
                    m = len(node.keys)
                    value = node.keys[m // 2]

                    temp_node = Node(self.order)
                    temp_node.counts = node.counts
                    temp_node.keys = node.keys[m // 2 + 1:]
                    temp_node.pointers = node.pointers[m // 2 + 1:]
                    node.keys = node.keys[:m // 2]
                    node.pointers = node.pointers[:m // 2 + 1]

                    s_node = Node(self.order)
                    s_node.keys.append(value)
                    s_node.counts[value] = 1
                    s_node.pointers.append(node)
                    s_node.pointers.append(temp_node)
                    self.root = s_node
                    return [None, None, None]
                else:
                    node.counts[temp[0]] = 1
                    node.pointers.insert(val_index+1, temp[2])
                    return [None, None, None]

    def insert(self, value):
        if (self.root == None):
            self.root = Node(self.order)
            self.root.keys.append(value)
            self.root.counts[value] = 1
            self.root.isLeaf = True
            return
        else:
            if(not self.search(value)):
                self.split(value, self.root)
            return


if (len(sys.argv) < 2):
    print("Enter filename")
    exit(0)
filename = sys.argv[1]

f = open("output.txt", 'w')

if not os.path.exists(filename):
    print("File doesn't exists")
    exit(0)

with open(filename, "r") as fp:
    obj = BPlusTree(3)
    for line in fp:
        l = line.split(" ")
        if (l[0] == "INSERT"):
            obj.insert(int(l[1]))
        elif (l[0] == "FIND"):
            temp = obj.find(int(l[1]))
            print(temp)
            f.write(str(temp)+"\n")
        elif (l[0] == "COUNT"):
            temp = (obj.count(int(l[1])))
            print(temp)
            f.write(str(temp)+"\n")
        elif (l[0] == "RANGE"):
            temp = (obj.range(int(l[1]), int(l[2])))
            print(temp)
            f.write(str(temp)+"\n")


f.close()
