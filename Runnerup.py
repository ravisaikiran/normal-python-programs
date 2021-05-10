Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given  scores. Store them in a list and find the score of the runner-up.
Output Format
Print the runner-up score.
Sample Input 0
5
2 3 6 6 5
Sample Output 0
5
solution:
  if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    winner=max(arr)
    second=[]
    for i in arr:
        if i!=winner:
            second.append(i)
    runner=max(second)
    print(runner)
