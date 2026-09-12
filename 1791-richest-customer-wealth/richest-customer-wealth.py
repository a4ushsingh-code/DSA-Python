class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth = []
        for account in accounts:
            maxwealth.append(sum(account))

        return max(maxwealth)
        