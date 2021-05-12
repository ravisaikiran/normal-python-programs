Consider a list (list = []). You can perform the following commands:

1.insert i e: Insert integer e at position i.
2.print: Print the list.
3.remove e: Delete the first occurrence of integer e.
4.append e: Insert e integer  at the end of the list.
5.sort: Sort the list.
6.pop: Pop the last element from the list.
7.reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above.
Iterate through each command in order and perform the corresponding operation on your list.
Sample Input :
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output :
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
solution:
  def fun(line,result):
    if(line[0]=="insert"):
        result.insert(int(line[1]),int(line[2]))
        return result
    elif(line[0]=="print"):
        print(result)
        return result
    elif(line[0]=='remove'):
        result.remove(int(line[1]))
        return result
    elif(line[0]=='append'):
        result.append(int(line[1]))
        return result
    elif(line[0]=='pop'):
        result.pop()
        return result
    elif(line[0]=='sort'):
        result.sort()
        return result
    elif(line[0]=='reverse'):
        return result[::-1]
        
        
        
if __name__ == '__main__':
    N = int(raw_input())
    result=[]
    for i in range(N):
        line=raw_input().split(' ')
        result=fun(line,result)
