"""
https://www.hackerrank.com/challenges/find-a-string/problem

Output Format
Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input
ABCDCDC
CDC

Sample Output
2
"""

string = "ABCDCDCDC"
sub_str = "CDC"

def count_substring(string, sub_str):
    count = 0
    for i in range(len(string) - len(sub_str) + 1):
        if string[i: i+len(sub_str)] == sub_str:
            count += 1
    return count

print(count_substring(string, sub_str))
