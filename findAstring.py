In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.
NOTE: String letters are case-sensitive.
Input Format
The first line of input contains the original string. The next line contains the substring.
Each character in the string is an ascii character.
Output Format
Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input:
ABCDCDC
CDC
Sample Output:
2
solution:
  def count_substring(string, sub_string):
    count=0
    l=len(sub_string)
    for i in range(0,len(string)):
        if(string[i:i+l]==sub_string):
            count+=1
    return count

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count
