The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
  Print the average of the marks array for the student name provided, showing 2 places after the decimal.
  Sample Input :
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output 0
56.00 #which is (52+56+60)/3)
solution:
  if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    sum=0.0
    n=0.0
    for i in student_marks[query_name]:
        sum+=i
        n+=1
    print("{0:.2f}".format(sum/n))
