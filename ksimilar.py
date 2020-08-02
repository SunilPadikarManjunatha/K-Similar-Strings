class Solution:
    def kSimilarity(self, A: str, B: str) -> int:

        a = list(A)
        b = list(B)
        k = 0

        queue = []
        queue.append(A)
        result = {A:0}
        i=0
        while queue:
            string = queue.pop()
            items = self.get_poss_swaps(list(string),b)
            if string == B: return result[string]
            for item in items:
                if item not in result:
                    result[item] = result[string] + 1
                    queue.append(item)
                    print(result)

    
    def get_poss_swaps(self, arr, b):
        
        for i, char in enumerate(arr):
            if char != b[i]:
                break
        poss_list = []
        for j in range(i+1, len(arr)):
            if arr[j] == b[i]:
                arr[j], arr[i] = arr[i], arr[j]
                poss_list.append("".join(arr))
                arr[i], arr[j] = arr[j], arr[j]

        return poss_list

sol = Solution()
A = "abccaacceecdeea"
B = "bcaacceeccdeaae"
print(sol.kSimilarity(A,B))

A = "ab"
B = "ba"
print(sol.kSimilarity(A,B))