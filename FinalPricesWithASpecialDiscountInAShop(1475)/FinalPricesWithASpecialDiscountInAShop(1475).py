# my first answer(not the best solution)
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices), 1):
                if prices[i] >= prices[j]:
                    prices[i] -= prices[j]
                    break

        return prices
      
# sample solution from https://www.youtube.com/watch?v=PW9jKsNVA1Y
# class Solution:
#     def finalPrices(self, prices: List[int]) -> List[int]:
#         stack = []

#         for i, price in enumerate(prices):
#             while stack and prices[stack[-1]] >= price:
#                 edit_idx = stack.pop()
#                 prices[edit_idx] -= price
#             stack.append(i)
        
#         return prices