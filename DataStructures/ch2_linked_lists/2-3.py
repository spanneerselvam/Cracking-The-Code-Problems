#Implement an algorithm to find the kth to last element of a singly linked list
import Node from linked_list
import LinkedList from linked_list
def delete_middle(LinkedList):
    middle = int(LinkedList.length()//2)
    LinkedList.erase(middle)

a = LinkedList()
s = "FOLLOW UP"
my_list = []
for ch in s:
    a.append(ch)
delete_middle(a)
a.display()
