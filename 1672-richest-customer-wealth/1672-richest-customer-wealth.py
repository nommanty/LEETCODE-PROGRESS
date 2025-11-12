class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account_list in accounts:
            current_wealth = 0
            for account_money in account_list :
                current_wealth = current_wealth + account_money
            if max_wealth <= current_wealth:
                max_wealth = current_wealth
        return max_wealth    