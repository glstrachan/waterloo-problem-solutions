#include <bits/stdc++.h>
using namespace std;

double best = -1000000;
vector<double> best_subset;
vector<double> s = {-1.0, -2.0, -3.0, -4.0, -5.0};

void make_set(vector<double> subset, vector<bool> chosen)
{
	if(subset.size() == 4)
	{
		double w = subset[0], x = subset[1], y = subset[2], z = subset[3];
		double sum = pow(w, x) + pow(y, z);

		if(sum > best) 
		{
			best = sum;
			best_subset = subset;
		}
		
	}
	else
	{
		for(int i = 0; i < s.size(); i++)
		{
			if(!chosen[i])
			{
				subset.push_back(s[i]);
				chosen[i] = true;
				make_set(subset, chosen);

				chosen[i] = false;
				subset.pop_back();
			}
		}
	}
}

int main()
{
	vector<double> subset;
	vector<bool> chosen(s.size());
	
	make_set(subset, chosen);
	printf("set: ");
	for(int i = 0; i < best_subset.size(); i++)
	{
		printf("%.0f%c ", best_subset[i], (i != best_subset.size() - 1 ? ',' : ' '));
	}

	printf("\nsum: %f", best);

	return 0;
}