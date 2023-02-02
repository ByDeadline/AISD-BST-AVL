import time

class Node:
    def __init__(self, value = None):
        self.left = None
        self.right = None
        self.value = value
        self.bf = 0
class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.ins(value,self.root)

    def ins(self, value, cur_node):
         if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left=Node(value)
            else:
                self.ins(value,cur_node.left)
         else:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self.ins(value, cur_node.right)

    def inorder(self):
        if self.root:
            self._print(self.root.left)
            print(self.root.value, end=" ")
            self._print(self.root.right)


    def _print(self,curNode):
        if not curNode:
            return

        if curNode.value is None:
            return

        if curNode.left is not None:
            self._print(curNode.left)
            print(curNode.value,end=" ")

        if curNode.right is not None:
            if curNode.left is None:
                print(curNode.value,end=" ")
            self._print(curNode.right)
            return 0

        if curNode.left is None and curNode.right is None:
            print(curNode.value,end=" ")

    def FindMax(self,CurNode = None):
        if CurNode is None:
            CurNode = self.root
        if CurNode.right is not None:
            print(CurNode.value,end=" ")
            self.FindMax(CurNode.right)
        if CurNode.right is None:
            print("Max to",CurNode.value)

    def FindMin(self,CurNode = None):
        if CurNode is None:
            CurNode = self.root
        if CurNode.left is not None:
            print(CurNode.value,end=" ")
            self.FindMin(CurNode.left)
        if CurNode.left is None:
            print("Min to",CurNode.value)

    def Balance(self,curNode = None):
        if curNode is None :
            curNode = self.root
        if curNode.right:
            self.Balance(curNode.right)
            curNode.bf -= 1
            curNode.bf -= curNode.right.bf
        if curNode.left:
            self.Balance(curNode.left)
            curNode.bf += 1
            curNode.bf += curNode.left.bf
        if not curNode.left and curNode.right:
            curNode.bf = 0

    def Delete(self,key):
        parent = None
        curNode = self.root
        #find coresponding Node and its parent
        while key!= curNode.value :
            if key >= curNode.value:
                parent = curNode
                curNode = curNode.right
            else :
                parent = curNode
                curNode = curNode.left
        # 1. no children
        if curNode.right is None and curNode.left is None:
            if curNode.value >= parent.value:
                parent.right = None
            else:
                parent.left = None
        # 2. one child
        elif curNode.left is None and curNode.right is not None:
            curNode.value = curNode.right.value
            curNode.right = None
        elif curNode.left is not None and curNode.right is None:
            curNode.value = curNode.left.value
            curNode.left = None
        # 3. two children
        elif curNode.left is not None and curNode.right is not None:
            # find min in the right branch
            temp = curNode.right
            while temp.left:
                temp = temp.left
            tempp=temp.value
            self.Delete(temp.value)
            curNode.value = tempp
            
    def PreOrder(self,root):
        if type(root) == type(1):
            key = root
            curNode = self.root
            while key!= curNode.value :
                if key>= curNode.value:
                    curNode = curNode.right
                else :
                    curNode = curNode.left
            root = curNode
        if root:
            print(root.value,end=" ")
            self.PreOrder(root.left)
            self.PreOrder(root.right)
    def PostOrder(self,root):
        if root:
            self.PostOrder(root.left)
            self.PostOrder(root.right)
            print(root.value,end=" ")

    def _FindMin(self, CurNode=None):
        if CurNode is None:
            CurNode = self.root
        if CurNode.left is not None:
            self._FindMin(CurNode.left)
        if CurNode.left is None:
            val = CurNode.value
            self.Delete(CurNode)
            return val

    def bfs(self):
        queue = [self.root]
        values = []
        while len(queue) > 0:
            cur_node = queue.pop(0)
            values.append(cur_node.value)
            if cur_node.left is not None:
                queue.append(cur_node.left)


            if cur_node.right is not None:
                queue.append(cur_node.right)
        print(values)

    def deleteTree(self,cur_Node ):
        if cur_Node is not None:
            self.deleteTree(cur_Node.left)
            self.deleteTree(cur_Node.right)
            print(cur_Node.value)
            cur_Node.left = None
            cur_Node.right = None
            cur_Node.value = None

def create_avl(arr):
    if len(arr) > 1:
        index = (len(arr) - 1) // 2
        tree.insert(arr[index])
        create_avl(arr[:index])
        create_avl(arr[index + 1:])
        return 0
    if len(arr) == 1:
        tree.insert(arr[0])

#driver Code
print ("jakie drzewo stworzyc :\n1) avl\n2) bst")
drzewo = input()

if drzewo == "1":
    arr = []
    arr = [int(x) for x in input().split()]
    arr.sort()
    tree = BST()
    create_avl(arr)
    tree.Balance()

if drzewo == "2":
    arr = [int(x) for x in input().split()]
    tree = BST()
    for x in arr:
        tree.insert(x)
    tree.Balance()
print(tree.root.bf)
while True:
    print("wybierz akcje :\n1) znajdz min i max\n2) usun element\n3) wypisz elementy in-order\n4) wypisz elementy post-order\n5) usuniecie drzewa\n6) wypisz poddrzewo\n7) równowarzenie drzewa\n8) stop")
    act = input()
    if act == '1':
        tree.FindMin()
        tree.FindMax()
    if act == '2':
        print("podaj element który chcesz usunąć")
        a = int(input())
        tree.Delete(a)
        print
    if act == '3':
        t1 = time.time()
        tree.inorder()
        t2 = time.time()
        print(t2-t1)
    if act == '4':
        tree.PostOrder(tree.root)
    if act == '5':
        tree.deleteTree(tree.root)
        del tree
    if act == '6':
        print("podaj korzeń")
        tree.PreOrder(input())
    if act == "7":
        while tree.root.bf != 0:
            temp = tree.root.value
            tree.Delete(temp)
            tree.insert(temp)
            tree.Balance()
    if act == "stop":
        break 
    print()
