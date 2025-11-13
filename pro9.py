9.	Search a Substring in a string by using Navie Algorithm.  
Aim: To Search a Substring in a string by using Navie Algorithm.
Description: 
The naive string searching algorithm is the simplest approach to finding a pattern within a given text. The idea is to align the pattern at the beginning of the text and check character by character to see if the entire pattern matches. If a mismatch occurs at any position, the algorithm shifts the pattern by one character to the right and repeats the process. This continues until the end of the text is reached.
Program:
def search_pattern(pattern, text):
    m = len(pattern)
    n = len(text)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            print(f"Pattern found at index {i}")
if __name__ == "__main__":
    text1 = input("Enter the Text: ")
    pattern1 = input("Enter the Pattern: ")
    search_pattern(pattern1, text1)
Output:
Enter the Text: AI&ML students comes to IR Lab
Enter the Pattern: students
Pattern found at index 6
