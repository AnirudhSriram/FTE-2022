class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        #Time = O(n) for base and O(3^m) for toppings as each toppings has 3 possibilities (0,1,2) = O(n * 3^m)
        # Space = O(3^n) for a ternary tree
        def dfs(toppingIndex, currCost):
            nonlocal cost
            if currCost==target:
                cost = currCost
                return cost
            if (abs(target-currCost)<abs(target-cost)) or ((abs(target-currCost)==abs(target-cost)) and currCost<cost):
                cost = currCost
            if currCost>target:
                return
            if toppingIndex==len(toppingCosts):
                return
            for i in range(3):
                dfs(toppingIndex+1, currCost+toppingCosts[toppingIndex]*i)
            
        cost = sys.maxsize
        for base in baseCosts:
            dfs(0,base)
        return cost