#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int minCostClimbingStairs(std::vector<int>& cost) {
    int n = cost.size();
    vector<int> dp(n + 1, 0);

    for (int i = 2; i <= n; ++i) {
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
    }

    return dp[n];
}

int main() {
    vector<int> cost1 = { 10, 15, 20 };
    vector<int> cost2 = { 1, 100, 1, 1, 1, 100, 1, 1, 1, 100, 1 };

    int minCost1 = minCostClimbingStairs(cost1);
    int minCost2 = minCostClimbingStairs(cost2);

    cout << "Example 1: " << minCost1 << endl;
    cout << "Example 2: " << minCost2;
    return 0;
}