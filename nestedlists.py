Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
  Output Format
Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.
Sample Input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output :
Berry
Harry
solution:
dic={}
s=[]
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    if score in dic:
        dic[score].append(name)
    else:
        dic[score]=[name]
    if score not in s:
        s.append(score)
x=min(s)
s.remove(x)
y=min(s)
dic[y].sort()
for i in dic[y]:
    print(i)
    
