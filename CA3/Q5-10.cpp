#include <iostream>
#include <vector>
using namespace std;

struct Node {
    int key;
    int priority;
    int index;
    Node *parent;
    Node *left;
    Node *right;
};

typedef Node* NodePointer;

class Treap
{
private:
	NodePointer root;
  vector<NodePointer> nodes;

	// AVL left rotate
	void leftRotate(NodePointer x) {
		NodePointer y = x->right;
		x->right = y->left;
		if (y->left != nullptr) {
			y->left->parent = x;
		}
		y->parent = x->parent;
		if (x->parent == nullptr) {
			this->root = y;
		} else if (x == x->parent->left) {
			x->parent->left = y;
		} else {
			x->parent->right = y;
		}
		y->left = x;
		x->parent = y;
	}

	// AVL right rotate
	void rightRotate(NodePointer x) {
		NodePointer y = x->left;
		x->left = y->right;
		if (y->right != nullptr) {
			y->right->parent = x;
		}
		y->parent = x->parent;
		if (x->parent == nullptr) {
			this->root = y;
		} else if (x == x->parent->right) {
			x->parent->right = y;
		} else {
			x->parent->left = y;
		}
		y->right = x;
		x->parent = y;
	}

	void moveUp(NodePointer x) {
		if (x->parent == nullptr) {
			return;
		}
		if (x->parent != nullptr && x->priority >= x->parent->priority) {
			return;
		}

		if (x == x->parent->left) {
			rightRotate(x->parent);
		} else {
			leftRotate(x->parent);
		}

		moveUp(x);
	}

	void moveDown(NodePointer x) {
		if (x->left == nullptr && x->right == nullptr) {
			return;
		}

		if (x->left != nullptr && x->right != nullptr) {
			if (x->left->priority < x->right->priority) {
				rightRotate(x);
			} else {
				leftRotate(x);
			}
		} else if (x->left != nullptr) {
			rightRotate(x);
		} else {
			leftRotate(x);
		}

		moveDown(x);
	}

public:
	Treap() {
		root = nullptr;
	}
  
  void print()
  {
    for(int i = 0;i < nodes.size(); i++)
    {
      if(nodes[i]->parent != nullptr)
        cout << nodes[i]->parent->index << " ";
      else
        cout << "0" << " ";
      
      if(nodes[i]->left != nullptr)
        cout << nodes[i]->left->index << " ";
      else
        cout << "0" << " ";
      
      if(nodes[i]->right != nullptr)
        cout << nodes[i]->right->index;
      else
        cout << "0";

      cout << endl;

    }
  }

	void insert(int key, int priority, int index) {
		NodePointer node = new Node;
    nodes.push_back(node);
		node->parent = nullptr;
		node->left = nullptr;
		node->right = nullptr;
		node->key = key;
		node->priority = priority;
    node->index = index;
		NodePointer y = nullptr;
		NodePointer x = this->root;

		while (x != nullptr) {
			y = x;
			if (node->key < x->key) {
				x = x->left;
			} else {
				x = x->right;
			}
		}

		node->parent = y;
		if (y == nullptr) {
			root = node;
		} else if (node->key < y->key) {
			y->left = node;
		} else {
			y->right = node;
		}

		// rotate to fix the priorities.
		if (node->parent != nullptr) {
			moveUp(node);
		}
	}

	NodePointer getRoot(){
		return this->root;
	}

};

class AgreementTree 
{
public:
    AgreementTree()
    {
        t = Treap();
    }

    void run()
    {
        read_input();
        
        print_result();
    }

    void read_input()
    {
        cin >> n;
        for(int i = 1; i <= n; i++)
        {
            int key,priority;
            cin >> key >> priority;
            t.insert(key,priority,i);
        }
    }
private:
    Treap t;
    int n;

    void print_result()
    {
      cout << "YES" << endl;
      t.print();
    }
};

int main() {
  AgreementTree at = AgreementTree();
  at.run();
	return 0;
}