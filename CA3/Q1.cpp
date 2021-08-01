#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
using namespace std;

class OneEditDistance
{
public:
    OneEditDistance()
    {
        c[0] = 'a';
        c[1] = 'b';
        c[2] = 'c';
    }
    void read_input()
    {
        cin >> n;
        cin >> q;

        for(int i = 0;i < n; i++)
        {
            string x;
            cin >> x;
            int len = x.size();
            if (umap.find(len) == umap.end())
            {
                unordered_map<string,int> new_map;
                new_map[x] = 1;
                umap[len] = new_map;
            }
            else
            {
                umap[len][x] = 1;
            }
        }

        vector <string> req;
        for(int i = 0; i < q; q++)
        {
            string x;
            cin >> x;
            req.push_back(x);
        }

        for(int i = 0; i < q; q++)
        {
            if(one_edit_distance_exists(req[i]))
            {
                cout << "YES" << endl;
            }
            else{
                cout << "NO" << endl;
            }
        }
    }
private:
    int n,q;
    unordered_map<int, unordered_map<string,int> > umap;
    char c[3];
    bool one_edit_distance_exists(string s)
    {
        int len = s.length();
        for(int i = 0;i < s.size(); i++)
        {
            for(int j = 0; j < 3;j++)
            {
                string s2 = s;
                if (s[i] == c[j]) continue;
                s2[i] = c[j];
                if(umap[len][s2] == 1)
                    return true;     
            }
        }

        return false;
    }
};

int main()
{
    OneEditDistance t;
    t.read_input();
    return 0;
}