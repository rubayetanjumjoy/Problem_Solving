class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
         

class Linkedlist:
    def __init__(self,node):
        self.head=node
    def at_begining(self,data):
        new_node=Node(data)
        # shifting head to 1 step
        if self.head is not None:
            new_node.next=self.head
        # assign newnode at head
        self.head=new_node
    def at_last(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            current_node=self.head
            while current_node.next:
                current_node=current_node.next
                 
            current_node.next=newnode

    def find_middle(self):
        fast=self.head
        slow=self.head
        while fast and fast.next:
            
            fast=fast.next.next
            slow=slow.next

        return slow
    
    def remove(self,data):
        current_node=self.head
         
        if current_node.data== data:
            
            self.head=current_node.next
    
            
        else:
      
            while current_node.next:
                if current_node.next.data == data:
                    # print(current_node.data)
                    current_node.next=current_node.next.next
                    print(data,'removed')
                    break
                    
                    # print(current_node.next.next.data)
                
                # if current_node.data==data:
                # #    {1,->{2,->{3,->}}},
                # #    print("paise",current_node.data)
                # #    print(current_node.next.data,'shmnaer element')
                #    print(current_node.data)
                #    current_node=current_node.next
                
                
                current_node=current_node.next
                
    def print_data(self):
        current_node=self.head
       
        while current_node:
            print(current_node.data)
             
            current_node=current_node.next

    def reverse_list(self):
        current_node=self.head
        prev=None
        # 1->2->3->-4>null
        # next=2->
        # cur.next{->2}==None
        # prev(none)=1->
        # curr=2->
        while current_node:
            # saving temp as 2->
            next=current_node.next
            # 2-> set to null
            current_node.next=prev
            # prev=1->
            prev=current_node 
            # curr=2->
            current_node=next
            # 2->1->null
            

            
            
            
            

        return prev

         
            

# creating node
node=Node('1')
# creating linkedlist
li=Linkedlist(node)

li.at_last('2')
li.at_last('3')
li.at_last('4')

# li.remove('2')
# print('after removing')
# li.print_data()
# print('after reverse')
# head=li.reverse_list()

# while head:
#     print(head.data)
#     head=head.next
x=li.find_middle()
print(x.data,'a')
 
