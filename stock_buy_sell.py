'''
Stock Buy Sell to Maximize Profit
BestBuy initially always the first element of the array
MaxProfit initially 0
while iterating each element of array from 1 to n-1
    if the current element is greater than bestBuy
        update maxProfit with max of maxProfit and current element - bestBuy
    update bestBuy with min of bestBuy and current element
return maxProfit
'''
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 
    (price = 6),  profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed 
    because you must buy before you sell.
    """
    mp, bestBuy = 0, prices[0]
    for i in range(1, len(prices)):
        if prices[i] > bestBuy:
            mp = max(mp, prices[i]-bestBuy)
        bestBuy = min(bestBuy, prices[i])
    return mp

print('Ans:', maxProfit([7,1,5,3,6,4])) #5  