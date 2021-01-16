class Node:
    def __init__(self,ch = None):
        self.ch = ch
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
def InfixTraversal(cur):
    if cur.left is not None:
        InfixTraversal(cur.left)
    print(cur.ch,end = ", ")
    if cur.right is not None:
        InfixTraversal(cur.right)
    

postFix = ['2','3','4','+','*'] # len = 5

arrayOfPointer = []
# Create array of pointer containing all characters
for i in range(len(postFix)):
    newNode = Node(postFix[i])
    tree = Tree()
    tree.root = newNode # 2 
    arrayOfPointer.append(tree) 
    #print(arrayOfPointer[i].root.ch)
len = len(postFix)
i = 0

while i < len:
    cur = arrayOfPointer[i].root
    if cur.ch == "+" or cur.ch == "*":
        cur.left = arrayOfPointer[i-2].root
        print('left = ',cur.left.ch)
        cur.right = arrayOfPointer[i-1].root
        print('right = ',cur.right.ch)
        j = i # 0 1 2 = 3
        

        while j < len:
            print("array[j](1)  = ",arrayOfPointer[j-2].root.ch)
            arrayOfPointer[j-2].root = arrayOfPointer[j].root
            print("array[j](2)  = ",arrayOfPointer[j-2].root.ch)
            j+=1
        len -=2

        i -= 1
    else:
        i += 1
        print('i = ',i)
cur = arrayOfPointer[0].root
InfixTraversal(cur)
    