class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        #freq=Counter(orders)
        order=set()
        tables=set()
        freq={}

        for c ,t ,f,in orders:
            tables.add(int(t))
            num=int(t)
            order.add(f)
            freq.setdefault(num, {})
            freq[num][f]=freq[num].get(f,0)+1
        #print(freq)    
        sorted_t=sorted(list(tables))
        sorted_f=sorted(list(order))
        print(sorted_t)
        res=[["Table"]+sorted_f]
        print(res)
        for t in sorted_t:
            num=[str(t)]
            #print(num)
            for f in sorted_f:
                count=str(freq[t].get(f,0))
                print(count)
                num.append(str(freq[t].get(f,0)))
            res.append(num)
        return res        


         
            
