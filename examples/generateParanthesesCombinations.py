class Solution(object):
    
    def paranth(self, n, l, r, lop, s):
        if (l==n and r==n):
            lop.append(s)
        
        elif (l==r):
            newS = s + '('
            self.paranth(n, l+1, r, lop, newS)
        
        else:
            # l>r
            if (l==n):
                # all left brackets done. So only right ones now.
                newS = s + ')'
                self.paranth(n, l, r+1, lop, newS)
            else:
                # left and right for remaining
                for i in range(0,2):
                    if i==0:
                        # go for left one.
                        newS = s + '('
                        self.paranth(n, l+1, r, lop, newS)
                    else:
                        # go for right one.
                        newS = s + ')'
                        self.paranth (n, l, r+1, lop, newS)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = 0
        r = 0
        lop = []
        s = ""
        self.paranth(n, l, r, lop, s)
        
        return lop      