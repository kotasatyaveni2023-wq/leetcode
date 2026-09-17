class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []

        for i in range(len(prices)):
            found = False

            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    result.append(prices[i] - prices[j])
                    found = True
                    break

            if not found:
                result.append(prices[i])

        return result
        