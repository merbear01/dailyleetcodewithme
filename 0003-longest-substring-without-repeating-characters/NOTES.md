
1. Initialize variables:
2. left: A pointer representing the left boundary of the current substring.
3. max_length: The maximum length of the non-repeating substring encountered so far.
4. char_set: An empty set to keep track of characters encountered.
5. Iterate through the string using the right pointer:
  If the character at s[right] is not in the char_set, add it to the set and update max_length if needed.
  If the character is already in the set, remove the character at s[left] from the set and move the left pointer one step to the right.
6. Repeat step 2 until the right pointer reaches the end of the string.

   
The final value of max_length will be the length of the longest substring without repeating characters.​
