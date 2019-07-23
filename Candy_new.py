class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        need=[1]*len(ratings)
        forward=[]
        backward=[]
        for i in range(len(ratings)):
            for j in range(i+1,len(ratings)):
                count=0
                if ratings[i]>ratings[j] and ratings[j]!=ratings[j+1]:
                    count+=1
                else:
                    break
                forward.append(count)
                count=0
            for k in range(-i-1,-len(ratings),-1):
                if ratings[-i-1]>ratings[k] and ratings[k]!=ratings[k-1]:
                    count+=1
                else:
                    break
                backward.append(count)
                count=0
        new=[(1+max[forward[i],backrward[i]]) for i in range(len(ratings))]
        print(new)