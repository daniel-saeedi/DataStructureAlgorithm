#!/usr/bin/env python
# coding: utf-8

# In[52]:


class TreapNode(object):
    def __init__(self, key, priority,index):
        self.key = key
        self.priority = priority
        self.index = index
        self.size = 1
        self.cnt = 1
        self.left = None
        self.right = None
        self.parent = None

    def left_rotate(self):
        a = self
        b = a.right
        a.right = b.left
        b.left = a
        a = b
        b = a.left
        b.size = b.left_size() + b.right_size() + b.cnt
        a.size = a.left_size() + a.right_size() + a.cnt
        return a

    def right_rotate(self):
        a = self
        b = a.left
        a.left = b.right
        b.right = a
        a = b
        b = a.right
        b.size = b.left_size() + b.right_size() + b.cnt
        a.size = a.left_size() + a.right_size() + a.cnt
        return a

    def left_size(self):
        return 0 if self.left is None else self.left.size

    def right_size(self):
        return 0 if self.right is None else self.right.size


class Treap(object):
    def __init__(self):
        self.root = None
        self.nodes = []

    def _insert(self, node, key, priority, index):
        if node is None:
            node = TreapNode(key, priority, index)
            self.nodes.append(node)
            return node
        node.size += 1
        if key < node.key:
            node.left = self._insert(node.left, key, priority, index)
            if node.left.ran < node.ran:
                node = node.right_rotate()
            
            node.left.parent = node
        elif key >= node.key:
            node.right = self._insert(node.right, key, priority, index)
            if node.right.ran < node.ran:
                node = node.left_rotate()
            node.right.parent = node
        return node

    def insert(self, key, priority,index):
        self.root = self._insert(self.root, key, priority, index)
    
    def insertBST(self,key,priority,index):
        new_node = TreapNode(key,priority,index)
        self.nodes.append(new_node)
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
                new_node.right_rotate()
            # If the new_node is inserted at right child, then do left rotation on this node
            else :
                new_node.left_rotate()
    
    def size(self):
        return 0 if self.root is None else self.root.size
    
    def print(self) :
        for node in self.nodes :
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


# In[53]:


# t = Treap()
# t.add(2,3,1)
# t.add(1,5,2)
# t.add(3,8,3)

# t.print()


# In[ ]:


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

main()
# In[ ]:




