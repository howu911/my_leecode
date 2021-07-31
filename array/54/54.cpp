/*
 * @Description: 54 ÂÝÐý¾ØÕó
 * @Version: 1.0
 * @Autor: laijiatao
 * @Date: 2021-07-29 22:45:22
 * @LastEditors: laijiatao
 * @LastEditTime: 2021-07-31 22:32:45
 */
#include <vector>
#include <iostream>

using namespace std;


class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int xMin = 0, xMax = matrix[0].size() - 1;
		int yMin = 0, yMax = matrix.size() - 1;
		int xZheng = 1, yZheng = 1;
		int all = (xMax + 1) * (yMax + 1);
		vector<int> output;

        if (xMax == 0)
		{
			for (int i = 0; i < yMax + 1; i++)
			{
				output.push_back(matrix[i][yMin]);
			}
			return output;
		}

        if (yMax == 0)
		{
			for (int i = 0; i < xMax +1; i++)
			{
				output.push_back(matrix[xMin][i]);
			}
			return output;
		}

		for (int x = xMin, y = yMin, count = 0; count < all;) {
			if (xZheng) {
				if (yZheng) {
					
					output.push_back(matrix[y][x]);
					count++;
					if (x == xMax) { xZheng = 0; x--; y++; }
					x++;
				}
				else {
					
					output.push_back(matrix[y][x]);
					count++;
					if (y == yMin) { yZheng = 1; y++; x++; }
					y--;
				}
			}
			else {
				if (yZheng) {
					
					output.push_back(matrix[y][x]);
					count++;
					if (y == yMax) { yZheng = 0; y--; x--; }
					y++;
				}
				else {
					
					output.push_back(matrix[y][x]);
					count++;
					if (x == xMin) { xZheng = 1; x++; y--; }
					x--;
				}
			}

			if (x == xMin && y == (yMin + 1) && count < all) {
				output.push_back(matrix[y][x]);
                count++;

                xMin++;     yMin++;
				xMax--;     yMax--;
				x = xMin;   y = yMin;

                if (xMax - xMin == 0)
                {
                    for (int i = yMin; i < yMax + 1; i++)
                    {
                        output.push_back(matrix[i][yMin]);
                    }
                    return output;
                }

                if (yMax - yMin == 0)
                {
                    for (int i = xMin; i < xMax +1; i++)
                    {
                        output.push_back(matrix[xMin][i]);
                    }
                    return output;
                }

				
			}

		}

		return output;
    }
};


int main(int argc, char **argv) {
    vector<vector<int>> matrix = {{1,2,3},{4,5,6},{7,8,9}};
    Solution s;

    vector<int> result;

    result = s.spiralOrder(matrix);

    for(int i = 0; i <result.size(); i ++) {
        cout << result[i] << " ";
    }

    cout << endl;  
    
}

