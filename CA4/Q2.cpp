#include <iostream>
#include <vector>
using namespace std;

class AliceTree
{
public:
    AliceTree(int _n) : n(_n) 
    {
        vector<int> adj[_n];
    }

    void addEdge(int u, int v)
    {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
private:
    int n;
    vector<int> adj;
};

void run()
{

}

int main()
{
    AliceTree at(10);
    return 0;
}