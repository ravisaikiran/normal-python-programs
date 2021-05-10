Let's learn about list comprehensions! You are given three integers x,y and z  representing the dimensions of a cuboid along with an integer n . 
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of (i+j+k) is not equal to n. Here,0<=i<=x ,0<=j<=y ,0<=k<=z Please use list comprehensions rather than multiple loops, as a learning exercise.

Examplez
1(x)
1(y)
1(z)
2(n)
All permutations of  are:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
solution:
  if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    results=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if(i+j+k!=n):
                    results.append([i,j,k])
    print(results)
