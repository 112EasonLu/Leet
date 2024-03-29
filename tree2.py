class BinarySearchTree:
    # This is a Node class that is internal to the BinarySearchTree class. 
    class Node:
        def __init__(self,val,left=None,right=None):
            self.val = val
            self.left = left
            self.right = right
            
        def getVal(self):
            return self.val
        
        def setVal(self,newval):
            self.val = newval
            
        def getLeft(self):
            return self.left
        
        def getRight(self):
            return self.right
        
        def setLeft(self,newleft):
            self.left = newleft
            
        def setRight(self,newright):
            self.right = newright
            
        # This method deserves a little explanation. It does an inorder traversal
        # of the nodes of the tree yielding all the values. In this way, we get
        # the values in ascending order.
        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem
                    
            yield self.val
            
            if self.right != None:
                for elem in self.right:
                    yield elem

        def __repr__(self):
            return "BinarySearchTree.Node(" + repr(self.val) + "," + repr(self.left) + "," + repr(self.right) + ")"            
            
    # Below are the methods of the BinarySearchTree class. 
    def __init__(self, root=None):
        self.root = root
        
    def insert(self,val):
        self.root = BinarySearchTree.__insert(self.root,val)
        
    def __insert(root,val):
        if root == None:
            return BinarySearchTree.Node(val)
        
        if val < root.getVal():
            root.setLeft(BinarySearchTree.__insert(root.getLeft(),val))
        else:
            root.setRight(BinarySearchTree.__insert(root.getRight(),val))
            
        return root
        
    def __iter__(self):
        if self.root != None:
            return iter(self.root)
        else:
            return iter([])

    def __str__(self):
        return "BinarySearchTree(" + repr(self.root) + ")"
 
def main():
    s = input("Enter a list of numbers: ")
    lst = s.split()
    
    tree = BinarySearchTree()
    
    for x in lst:
        tree.insert(float(x))
        
    for x in tree:
        print(x)

if __name__ == "__main__":
    main()




def printInorder(root,a): 
    if root:   
        a.append(root.val)
        printInorder(root.next,a)
    return a

def ful(ori_list,k):
    m=[1,2,3]
    bo=len(ori_list)
    if bo <= k:
        for i in range(k-bo):
             ori_list.append(int(0))
    return ori_list
          
#class Solution:

#class Solution:
  #  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
          #def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
  #      b,c=[],[]
   #     printInorder(l1,b)
   #     printInorder(l2,c)
       # print(b,c)
      #  ful(b), ful(c)
        #print(b,c)
     #   value=(b[0]+c[0])+10*(b[1]+c[1])+100*(b[2]+c[2])
      #  value_s=str(value)
      ##  ans=ListNode(int(value_s[2]))
       # ans.next=ListNode(int(value_s[1]))
       # ans.next.next=ListNode(int(value_s[0]))

     #   return b
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        b,c=[],[]
        printInorder(l1,b)
        printInorder(l2,c)
        len(b),len(c)
        k=max(len(b),len(c))
        ful(b,k),ful(c,k)
        for i in range(k):
            n=0
            cal=b[i]+c[i]
            if cal >10:
                
        value=(b[0]+c[0])+10*(b[1]+c[1])+100*(b[2]+c[2])
        value_s=str(value)
 #       ans=ListNode(int(value_s[2]))
#        ans.next=ListNode(int(value_s[1]))
#        ans.next.next=ListNode(int(value_s[0]))
        return l1