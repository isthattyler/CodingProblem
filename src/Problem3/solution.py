class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def serialize(self, root):
        string = ""
        if root == None:
            return "#"
        string += root.val + " "
        string += self.serialize(root.left) + " "
        string += self.serialize(root.right) + " "
        return string
 
    def deserialize(self, serial):
        value = serial.split(" ")
        def decode(values, i=0):
            j = i
            val = values[i]
            if val == "#":
                return None
            node = Node(val)
            node.left = decode(values, j+1)
            node.right = decode(values, j+1)
            return node
        return decode(value)

node = Node('root', Node('left', Node('left.left')), Node('right'))
serial = Solution().serialize(node)
print(serial)

if Solution().deserialize(serial).left.left.val == 'left.left':
    print(1)
else:
    print(0)