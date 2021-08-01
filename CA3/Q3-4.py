#!/usr/bin/env python
# coding: utf-8

# In[55]:


class Node :
    def __init__(self,_key, _priority,_index = 0,_parent = None) :
        self.key = _key
        self.priority = _priority
        self.index = _index
        self.parent = _parent
        self.right = None
        self.left = None


# In[111]:


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
    #AVL Left Rotation
    def leftRotate(self, node):
        if node.parent == self.root :
            self.root = node

        parent = node.parent

        node.parent = parent.parent

        if parent.parent != None: 
            parent.parent.right = node

        parent.right = node.left

        if parent.right != None :
            parent.right.parent = parent

        node.left = parent
        
        parent.parent = node
    
    #AVL Right Rotation
    def rightRotate(self, node):
        if node.parent == self.root :
            self.root = node

        parent = node.parent

        node.parent = parent.parent

        if parent.parent != None: 
            parent.parent.left = node

        parent.left = node.right

        if parent.left != None :
            parent.left.parent = parent

        node.right = parent
        
        parent.parent = node

    def print(self) :
        for node in self.l :
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
            


# In[112]:


t = Treap()
t.add(2,3,1)
t.add(1,5,2)
t.add(3,8,3)

# t.add(4,7,4)

# t.add(15,2,5)

# t.add(0.5,1,6)

t.print()


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


# main()


# In[ ]:




