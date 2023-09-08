class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def dfs(nlists):
            if len(nlists) == numRows:
                return nlists
            else:
                new_list = [1]
                nlist = nlists[-1]
                for i in range(0, len(nlist)-1):
                    new_list.append(nlist[i]+nlist[i+1])
                new_list.append(1)
                nlists.append(new_list)
                return dfs(nlists)

        init = [[1], [1,1]]
        if numRows == 1:
            return  [[1]]
        lists = dfs(init)
        return lists
