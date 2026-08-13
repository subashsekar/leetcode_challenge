class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        sort = sorted(prices)
        cost = sort[0] +sort[1]
        if cost <= money:
            return money - cost
        return money
