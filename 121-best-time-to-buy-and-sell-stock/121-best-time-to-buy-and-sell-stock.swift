class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
     
        let count  = prices.count
        //var lidx = 0
        var profit = 0

        var mini = prices[0]

         for i in 1..<count  {
            let cost = prices[i] - mini
            profit = max(profit, cost)
            mini =  min(prices[i], mini)
        }
    

        return profit
    }
}