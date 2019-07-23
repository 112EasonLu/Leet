class Solution:
    def candy(self, ratings: List[int]) -> int:
        bratings=[ratings[i] for i in range(-1,-len(ratings)-1,-1)]
        need=[]
        forward=[]
        backward=[]
        for i in range(len(ratings)):
            print('i:',i)
            for j in range(i+1,len(ratings)):
                print('j:',j)
                if j!=len(ratings)-1:
                    count,count1=0,0
                    if ratings[i]>ratings[j] and ratings[j]!=ratings[j+1]:
                        count+=1
                    else:break
                    if bratings[i]>bratings[j] and bratings[j]!=bratings[j+1]:
                        count1+=1
                    else:break
                else:
                    count,count1=0,0
                    if ratings[i]>ratings[j]:
                        count+=1
                    else:break
                    if bratings[i]>bratings[j]:
                        count1+=1
                    else:break
            forward.append(count)
            print('forward:',forward)
            backward.append(count1)
            print('backward:',backward)
        need=[(1+max(forward[i],backward[i])) for i in range(len(backward))]
        print(need)
        return sum(need)