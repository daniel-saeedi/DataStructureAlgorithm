#include <iostream>
#include <vector>
#include <unordered_map>
#include <utility>
using namespace std;

class Gloves
{
public:
    Gloves(int _n,int _m,int _k,vector<int> _colors) : n(_n),m(_m),k(_k),colors(_colors)
    {
        
    };

    void addEdge(int u,int v)
    {
        if(u == v) return;

        bool inserted = false;
        
        for(int i = 0;i < forest_gloves.size();i++)
        {
            if(inserted == true) break;

            bool u_exists = forest_gloves[i].find(u) != forest_gloves[i].end();
            bool v_exists = forest_gloves[i].find(v) != forest_gloves[i].end();
            if (!u_exists && !v_exists)
                continue;
            //There is no difference between (u,v) and (v,u)
            // if (u_exists && v_exists)
            //     inserted = true;
            //     break;
            if(u_exists) 
                forest_gloves[i][u] += 1;
            else
                forest_gloves[i][u] = 1;
            
            if(v_exists) 
                forest_gloves[i][v] += 1;
            else
                forest_gloves[i][v] = 1;
            if(max_elements[i].second < forest_gloves[i][v])
                max_elements[i].first = colors[v];
                max_elements[i].second = forest_gloves[i][v];
    
            if(max_elements[i].second < forest_gloves[i][u])
                max_elements[i].first = colors[u];
                max_elements[i].second = forest_gloves[i][u];
            inserted = true;

            //Might be buggy
            if (!(u_exists && v_exists))
                count_elements[i] += 2;
        }

        if(!inserted)
        {
            unordered_map<int,int> hash_table;
            hash_table[u] = 1;
            hash_table[v] = 1;
            forest_gloves.push_back(hash_table);
            pair<int,int> m;
            m.first = colors[u-1];
            m.second = 1;
            max_elements.push_back(m);
            count_elements.push_back(2);
        }
    }

    int calculateMinColoring()
    {
        int coloring = 0;
        for(int i = 0;i < forest_gloves.size();i++)
        {
            int max = max_elements[i].second;
            coloring += (count_elements[i]-max);
        }

        return coloring;
    }


private:
    int n;
    int m;
    int k;
    vector<int> colors;
    vector<unordered_map<int,int> > forest_gloves;
    vector<vector<int> > forest;
};

void run()
{
    int n,m,k;
    vector<int> colors;
    cin >> n >> m >> k;
    for(int i = 0;i < m; i++)
    {
        int x;
        cin >> x;
        colors.push_back(x);
    }
    Gloves g(n,m,k,colors);

    while(m > 0)
    {
        m--;
        int u,v;
        cin >> u >> v;
        g.addEdge(u-1,v-1);
    }
    
    cout << g.calculateMinColoring();
}

int main()
{
    run();
    // int n = 3;
    // int m = 2;
    // int k = 3;
    // vector<int> colors;
    // colors.push_back(1);
    // colors.push_back(2);
    // colors.push_back(3);
    // Gloves g(n,m,k,colors);

    // g.addEdge(1,2);
    // g.addEdge(2,3);

    // cout << g.calculateMinColoring();

    // int n = 3;
    // int m = 2;
    // int k = 2;
    // vector<int> colors;
    // colors.push_back(1);
    // colors.push_back(1);
    // colors.push_back(2);
    // Gloves g(n,m,k,colors);

    // g.addEdge(1,2);
    // g.addEdge(2,1);

    // cout << g.calculateMinColoring();

    return 0;
}