#include <iostream>
#include <vector>
using namespace std;

class Node
{
public:
    Node(int d,Node *n)
    {
        data = d;
        next = n;
    }
    int data;
    Node* next;
};

class LinkedList
{
public:
    LinkedList()
    {
        head = nullptr;
        last = nullptr;
    }

    void append(int x)
    {
        Node *new_node = new Node(x,nullptr);
        if(head == nullptr)
        {
            head = new_node;
            last = new_node;
        }
        else
        {
            last->next = new_node;
            last = new_node;
        }

        nodes.push_back(new_node);
    }

    void print_list()
    {
        Node *p = head;
        while( p != nullptr )
        {
            cout << p->data << " ";
            p = p->next;
        }
    }

    void move(int x,int y, int n)
    {
        Node *start = nodes[n-x];
        Node *last = nodes[n-1];
        if(y == 0)
        {
            last->next = head;
            head = start;
        }
        else
        {
            Node *y0 = nodes[y-1];
            Node *y1 = nodes[y];
            y0->next = start;
            last->next = y1;
        }
        nodes[n-x-1]->next = nullptr;

        vector<Node*>::const_iterator first = nodes.begin();
        vector<Node*>::const_iterator _y = nodes.begin()+y;
        vector<Node*>::const_iterator n_x = nodes.begin()+(n-x);
        vector<Node*>::const_iterator _last = nodes.end();

        vector<Node*> v;
        v.insert(v.begin(),first,_y);
        v.insert(v.end(),n_x,_last);
        v.insert(v.end(),_y,n_x);
        nodes = v;
    }
private:
    vector<Node*> nodes;
    Node *head;
    Node *last;
};

class Shuffler
{
public:
    Shuffler()
    {
        ll = LinkedList();
        a = 1103515245; 
        m = 2147483648; 
        c = 12345;
    }
    void read_input()
    {
        cin >> n;
        cin >> t;
        cin >> seed;
        for(int i = 1;i <= n;i++)
        {
            ll.append(i);
        }
    }

    void shuffle()
    {
        while(t > 0)
        {
            t--;
            int x = createRandom(0, n);
            int y = createRandom(0, n-x);
            if(x == 0) continue;
            if(x+y == n) continue;
            ll.move(x,y,n);
        }
        ll.print_list();
    }
private:
    LinkedList ll;
    int n;
    int t;
    long int seed;
    long int a; 
    long int m;
    int c;

    int RNG()
    {
        seed = (a * seed + c)%m;
        return seed;
    }

    int createRandom(int l,int r)
    {
        return (RNG() % (r-l+1))+ l; 
    }
};

int main()
{
    Shuffler shuffler = Shuffler();
    shuffler.read_input();
    shuffler.shuffle();
    return 0;
}