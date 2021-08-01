#include <iostream>
#include <vector>
#include <unordered_map>
#include <utility>
#include <algorithm>
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

        if(forest.size() == 0)
        {
            unordered_map<int,int> hash_table;
            hash_table[u] = 1;
            hash_table[v] = 1;
            forest.push_back(hash_table);
            
            unordered_map<int,int> color_freq;
            color_freq[colors[u-1]] += 1;
            color_freq[colors[v-1]] += 1;
            colors_freq_per_tree.push_back(color_freq);
        }
        else
        {
            // bool inserted = false;
            bool u_found = false;
            bool v_found = false;
            int first_tree_index = -1;
            int last_tree_index = -1;

            for(int i = 0;i < forest.size();i++)
            {
                if(!u_found) u_found = forest[i].find(u) != forest[i].end();
                if(!v_found) v_found = forest[i].find(v) != forest[i].end();

                if(u_found || v_found)
                {
                    if(first_tree_index == -1)
                    {
                        first_tree_index = i;
                        last_tree_index = i;
                    }
                        
                }
                //Might be buggy
                if(u_found && v_found)
                {
                    last_tree_index = i;
                    break;
                }
            }

            if(u_found && v_found)
            {
                if(forest[first_tree_index].find(u) != forest[first_tree_index].end() && forest[first_tree_index].find(v) != forest[first_tree_index].end()
                || forest[last_tree_index].find(u) != forest[last_tree_index].end() && forest[last_tree_index].find(v) != forest[last_tree_index].end() )
                    return;
            }

            //We have to combine two separate trees
            if(u_found && v_found && first_tree_index != last_tree_index)
            {
                unordered_map<int, int>::iterator it = forest[last_tree_index].begin();
                while(it != forest[last_tree_index].end())
                {
                    forest[first_tree_index][it->first] += it->second; 
                    it++;
                }
                forest.erase(forest.begin() + last_tree_index);

                unordered_map<int, int>::iterator it2 = colors_freq_per_tree[last_tree_index].begin();
                while(it2 != colors_freq_per_tree[last_tree_index].end())
                {
                    colors_freq_per_tree[first_tree_index][it2->first] += it2->second; 
                    it2++;
                }
                colors_freq_per_tree.erase(colors_freq_per_tree.begin() + last_tree_index);
            }
            else if((u_found || v_found))
            {
                if(!u_found)
                {
                    forest[first_tree_index][u] = 1;
                    colors_freq_per_tree[first_tree_index][colors[u-1]] +=  1;
                    
                }
                
                if(!v_found)
                {
                    forest[first_tree_index][v] = 1;
                    colors_freq_per_tree[first_tree_index][colors[v-1]] +=  1;
                    
                }

            }
            else
            {
                unordered_map<int,int> hash_table;
                hash_table[u] = 1;
                hash_table[v] = 1;
                forest.push_back(hash_table);
                
                unordered_map<int,int> color_freq;
                color_freq[colors[u-1]] += 1;
                color_freq[colors[v-1]] += 1;
                colors_freq_per_tree.push_back(color_freq);
            }
        }
    }

    int calculateMinColoring()
    {
        int coloring = 0;
        for(int i = 0;i < forest.size();i++)
        {
            unordered_map<int, int>::iterator it = colors_freq_per_tree[i].begin();
            int max = 0;
            while(it != colors_freq_per_tree[i].end())
            {
                if(it->second > max)
                {
                    max = it->second;
                }
                it++;
            }
            coloring += (forest[i].size()-max);
        }

        // cout << "Testing !!!!!!!!!!! " << endl;
        // unordered_map<int, int>::iterator it2 = colors_freq_per_tree[1].begin();
        // while(it2 != colors_freq_per_tree[1].end())
        // {
        //     cout << it2->first << " ";
        //     cout << it2->second << endl;
        //     it2++;
        // }

        // cout << endl;

        return coloring;
    }


private:
    int n;
    int m;
    int k;
    vector<int> colors;
    vector<unordered_map<int,int> > forest;

    vector<unordered_map<int,int> > colors_freq_per_tree;

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
        g.addEdge(u,v);
    }
    
    cout << g.calculateMinColoring();
}

int main()
{
    // run();
    int n = 8;
    int m = 4;
    int k = 8;
    vector<int> colors;
    colors.push_back(7);
    colors.push_back(2);
    colors.push_back(4);
    colors.push_back(3);
    colors.push_back(5);
    colors.push_back(6);
    colors.push_back(7);
    colors.push_back(7);
    colors.push_back(9);
    Gloves g(n,m,k,colors);

    g.addEdge(1,7);
    g.addEdge(2,1);
    g.addEdge(2,7);

    g.addEdge(3,4);

    g.addEdge(8,6);
    g.addEdge(8,9);
    g.addEdge(8,7);
     g.addEdge(7,8);

    cout << g.calculateMinColoring() << endl;

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