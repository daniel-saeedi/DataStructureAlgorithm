#include<iostream>
#include <unordered_map>
using namespace std;

class Node{
public:
    int key;
    int height;
    Node * left;
    Node * right;
    Node(int k){
        height = 1;
        key = k;
        left = nullptr;
        right = nullptr;
    }
};

class AVL
{
public:
    Node * root = nullptr;
    int n;
    unordered_map<int,int> m;
    void insert(int x){
        m[x] = x;
        root=_insert(root, x);
    }

    Node *search(int x){
        return _search(root,x);
    }
    
    bool exists(int x){
        if (m.find(x) == m.end())
            return false;
        return true; 
    }

    void inorder(){
        _inorder(root);
        cout<<endl;
    }

    int count_less_than(int x)
    {
        return _count_less_than(root,x);
    }
private:
    int height(Node * head){
        if(head==nullptr) return 0;
        return head->height;
    }

    int _count_less_than(Node *r,int x)
    {
        if(r == nullptr)
            return 0;
        int countLeft = _count_less_than(r->left, x);
        int countRight = 0;
        if(r->key <= x)
            countRight = _count_less_than(r->right, x);

        return (r->key < x ? 1 : 0) + countLeft + countRight;
    }

    Node *rightRotation(Node * head){
        Node * new_head = head->left;
        head->left = new_head->right;
        new_head->right = head;
        head->height = 1+max(height(head->left), height(head->right));
        new_head->height = 1+max(height(new_head->left), height(new_head->right));
        return new_head;
    }

    Node *leftRotation(Node * head){
        Node * new_head = head->right;
        head->right = new_head->left;
        new_head->left = head;
        head->height = 1+max(height(head->left), height(head->right));
        new_head->height = 1+max(height(new_head->left), height(new_head->right));
        return new_head;
    }

    void _inorder(Node * head){
        if(head==nullptr) return ;
        _inorder(head->left);
        cout<<head->key<<" ";
        _inorder(head->right);
    }

    Node * _insert(Node * head, int x){
        if(head==nullptr){
            n+=1;
            Node * temp = new Node(x);
            return temp;
        }
        if(x < head->key) head->left = _insert(head->left, x);

        else if(x > head->key) head->right = _insert(head->right, x);

        head->height = 1 + max(height(head->left), height(head->right));

        int b = height(head->left) - height(head->right);
        if(b>1){
            if(x < head->left->key){
                return rightRotation(head);
            }else{
                head->left = leftRotation(head->left);
                return rightRotation(head);
            }
        }else if(b<-1){
            if(x > head->right->key){
                return leftRotation(head);
            }else{
                head->right = rightRotation(head->right);
                return leftRotation(head);
            }
        }
        return head;
    }
    
    Node * _search(Node * head, int x){
        if(head == nullptr) return nullptr;
        int k = head->key;
        if(k == x) return head;
        if(k > x) return _search(head->left, x);
        if(k < x) return _search(head->right, x);
    }
};

void run()
{
    AVL t;
    int q;
    cin >> q;
    while(q > 0)
    {
        q--;
        int request_type,x;
        cin >> request_type >> x;
        if(request_type == 1)
            t.insert(x);
        // else if(request_type == 2)
        //     if (t.exists(x)) cout << "YES" << endl;
        //     else cout << "NO" << endl;
        // else
        //     cout << t.count_less_than(x) << endl;
    }
}

int main(){
    run();
}
