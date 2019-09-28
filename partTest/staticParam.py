class task_queue():
    queue=[]
    def append(self,obj):
        self.queue.append(obj)

    def print_queue(self):
        print(self.queue)

class sample():  
    num = 0  

if __name__=="__main__":
    a=task_queue()
    b=task_queue()
    c=task_queue()

    a.append('tc_1')

    a.print_queue()
    b.print_queue()
    c.print_queue()

    obj1 = sample()  
    obj2 = sample()   
    print(obj1.num, obj2.num, sample.num)
    obj1.num += 1  
    print(obj1.num, obj2.num, sample.num) 
    sample.num += 2  
    print(obj1.num, obj2.num, sample.num)