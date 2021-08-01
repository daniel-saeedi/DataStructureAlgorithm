#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Node :
    def __init__(self,_key, _priority,_index = 0,_parent = None) :
        self.key = _key
        self.priority = _priority
        self.index = _index
        self.parent = _parent
        self.right = None
        self.left = None


# In[12]:


class Treap :
    def __init__(self) :
        self.root = None
        self.l = []
    
    def insertBST(self,key,priority,index):
        new_node = Node(key,priority,index)
        self.l.append(new_node)
        if self.root == None :
            self.root = new_node
            return self.root
        
        current_node, prev_node = self.root, self.root
        
        while current_node != None :
            prev_node = current_node
            if current_node.key < key :
                current_node = current_node.right
            else :
                 current_node = current_node.left
        
        new_node.parent = prev_node
        if key > prev_node.key :
            prev_node.right = new_node
        else :
            prev_node.left = new_node
        return new_node

 
    def add(self,key,priority,index) :
        new_node = self.insertBST(key,priority,index)

        while 1 :
            if new_node.parent != None :
                if new_node.priority > new_node.parent.priority :
                    break
            else :
                break
            
            parent = new_node.parent
            # If the new_node is inserted at left child, then do right rotation on this node
            if parent.left == new_node :
                self.rightRotate(new_node)
            # If the new_node is inserted at right child, then do left rotation on this node
            else :
                self.leftRotate(new_node)

    #AVL Right Rotation
    def rightRotate(self, node):
        end = node
        while 1 :
            if end.parent != None and end.parent.left == end :
                end = end.parent
            else :
                break

        lchild = end.left

        if end == self.root :
             self.root = lchild

        if end.parent != None and end.parent.right == end :
            end.parent.right = lchild

        if lchild != None :
            lchild.parent = end.parent
            if lchild.right != None :
                lchild.right.parent = end

        if end != None :
            end.parent = lchild
            end.left = lchild.right
        if lchild != None :
            lchild.right = end
        
    def leftRotate(self, node) :
        end = node
        while 1 :
            if end.parent != None and end.parent.right == end :
                end = end.parent
            else :
                break

        rchild = end.right

        if end == self.root :
             self.root = rchild

        if end.parent != None and end.parent.left == end :
            end.parent.left = rchild

        if rchild != None :
            rchild.parent = end.parent
            if rchild.left != None :
                rchild.left.parent = end
                
        if end != None :
            end.parent = rchild
            end.right = rchild.right
        
        if rchild != None :
            rchild.left = end
    def print(self) :
        for node in l :
            s = ""
            if(node.parent == None) :
                s += "0 "
            else :
                s += str(node.parent.index) + " "
            
            if(node.left == None) :
                s += "0 "
            else :
                s += str(node.left.index) + " "
            
            if(node.right == None) :
                s += "0 "
            else :
                s += str(node.right.index)
            
            print(s)
            


# In[13]:


# t = Treap()

# t.add(12,1,1)
# t.add(10,1,1)
# t.add(15,1,1)
# t.add(16,1,1)
# t.add(13,1,1)
# t.add(14,1,1)


# In[ ]:





# In[113]:


def main() :
    t = Treap()
    n = int(input())
    for i in range(1,n+1) :
        key, priority = input().split()
        key = int(key)
        priority = int(priority)
        t.add(key,priority,i)
    print("YES")
    t.print()


# In[114]:


main()


# In[ ]:




