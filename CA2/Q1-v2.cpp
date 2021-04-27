#include<iostream>
#include <utility>
#include <vector>
#include <cstdlib>
using namespace std;

struct MaxHeap
{
    vector<int> data;
    MaxHeap()
    {
        data.push_back(0);
    }
    void insert(int value)
    {
        data.push_back(value);
        int current = data.size()-1;
        while(current != 1)
        {
            if(data[current] > data[current >> 1])
            {
                swap(data[current], data[current >> 1]);
                current >>= 1;
            }
            else break;
        }
    }
    void pop()
    {
        if(data.size() == 1) return;
        swap(data[1], data[data.size()-1]);
        data.pop_back();
        int current = 1;
        while(current < data.size())
        {
            int largest = current;
            if((current << 1) < data.size() && data[current << 1] > data[largest])
            {
                largest = current << 1;
            }
            if((current << 1) + 1 < data.size() && data[(current << 1) + 1] > data[largest])
            {
                largest = (current << 1) + 1;
            }
            if(largest != current)
            {
                swap(data[current], data[largest]);
                current = largest;
            }
            else break;
        }
    }
    int top()
    {
        return data[1];
    }
    bool empty()
    {
        return data.size() <= 1;
    }
};

class War
{
public:
	War()
	{
		MaxHeap attack_priorities = MaxHeap();
		min_moves = 0;

	}

	void read_input()
	{
		cin >> n;
		cin >> z;
		cin >> k;
		for(int i = 0;i < n;i++)
		{
			int power;
			cin >> power;
			attack_priorities.insert(power);
		}
	}

	void start()
	{
		while(z > 0 && min_moves < k)
		{
			int biggest_power = attack_priorities.top();
			attack_priorities.pop();
			z -= biggest_power;
			attack_priorities.insert(biggest_power/2);
			min_moves++;
		}

		if(z <= 0 && min_moves <= k)
			cout << min_moves << endl;
		else
			cout << -1 << endl;
	}
private:
	MaxHeap attack_priorities;
	long int n;
	long int z;
	long int k;
	long int min_moves;
};
int main()
{
	War war = War();
	war.read_input();
	war.start();
	return 0;
}