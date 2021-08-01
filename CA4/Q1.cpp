#include <iostream>
#include <tuple>
#include <vector>
#include <queue>
using namespace std;


struct Node 
{
	tuple <int, int, int> data;
	Node* next;
	Node(tuple <int, int, int> d)
	{
		data = d;
		next = NULL;
	}
};

struct Queue {
	Node *front, *rear;
	Queue()
	{
		front = rear = NULL;
	}
    //x arguments: (x,y,time)
	void enQueue(tuple <int, int, int> x)
	{
		Node* temp = new Node(x);

		if (rear == NULL) {
			front = rear = temp;
			return;
		}

		rear->next = temp;
		rear = temp;
	}

	void deQueue()
	{
		if (front == NULL)
			return;

		Node* temp = front;
		front = front->next;
    
		if (front == NULL)
			rear = NULL;

		delete (temp);
	}
};

class PristonBuilding
{
public:
    PristonBuilding(int _m,int _n,int _k) : m(_m), n(_n), k(_k){};
    void new_building(tuple <int, int, int> d)
    {
        q.push(d);
    }

    int start_simulation()
    {
        vector<vector<int>> matrix(n, std::vector<int>(m, 0));
        int directions[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};

        int time = 1;

        while(!q.empty())
        {
            tuple <int, int, int> current_node = q.front();
            q.pop();

            matrix[get<0>(current_node)][get<1>(current_node)] = 1;
            for(int i = 0;i < 4;i++)
            {
                tuple <int, int,int> adj_node;
                adj_node = make_tuple(directions[i][0] + get<0>(current_node), directions[i][1] + get<1>(current_node),0);
                if(!is_valid(adj_node))
                    continue;
                 if(matrix[get<0>(adj_node)][get<1>(adj_node)] == 1)
                    continue;
                time = get<2>(current_node) + 1;
                get<2>(adj_node) = time;
                matrix[get<0>(adj_node)][get<1>(adj_node)] = 1;
                new_building(adj_node);
            }
        }

        return time;
    }
private:
    int m;
    int n;
    int k;
    queue<tuple <int, int, int>> q;

    bool is_valid(tuple <int, int, int> pos)
    {
        return get<0>(pos) < n && get<1>(pos) < m and get<0>(pos) >= 0 && get<1>(pos) >= 0;
    }

};

void run()
{
    int m,n,k;
    cin >> m >> n >> k;
    PristonBuilding pb(m,n,k);

    int i = 0;
    while(i < 2*k)
    {
        int x,y;
        cin >> x >> y;
        tuple <int, int, int> building;
        building = make_tuple(x-1,y-1,1);
        pb.new_building(building);
        i += 2;
    }

    cout << pb.start_simulation() << endl;
}
int main()
{
    run();

}
