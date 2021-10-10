#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> merge1(vector<vector<int>>& intervals) {
    if (intervals.size() <= 1)
        return intervals;

    for (int i = 0; i < intervals.size(); ++i) {
        for (int j = i+1; j < intervals.size(); ++j) {
            if(intervals[j][1] < intervals[i][0]){
                vector<int> temp = intervals[i];
                intervals[i] = intervals[j];
                intervals[j] = temp;
                continue;
            }

            if(intervals[i][1] >= intervals[j][0]){
                intervals[i][1] = max(intervals[i][1], intervals[j][1]);
                intervals[i][0] = min(intervals[i][0], intervals[j][0]);
                intervals.erase(intervals.begin() + j);
                if (j <= 1)  
                    j++;
                j-=2;
                if (i == 0) 
                    continue;
                i--;
            }
        }
    }
    return intervals;
}


vector<vector<int>> merge(vector<vector<int>>& intervals) {
    if (intervals.size() <= 1)
        return intervals;

    vector<vector<int>> merged;
    sort(intervals.begin(), intervals.end());
    for (int i = 0; i < intervals.size(); i++) {
        if (merged.size() == 0 || merged.back()[1] < intervals[i][0]){
            merged.push_back(intervals[i]);
        }
        else {
            merged.back()[1] = max(merged.back()[1], intervals[i][1]);
        }
    }
    
    return merged;
}

int main() {
    vector<vector<int>> a = {{1,4},{0,2},{3,5}};
    vector<vector<int>> b= merge(a);
    for (int i = 0; i < b.size(); ++i){
        for (int j = 0; j < b[i].size(); ++j)
            cout << b[i][j] << " ";
        cout << endl;
    }
}