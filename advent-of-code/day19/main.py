def can_form_sentence(patterns, sentence):
    # Create a DP array of length len(sentence) + 1 (all initialized to False)
    dp = [False] * (len(sentence) + 1)
    dp[0] = 1  # base case: empty string can be formed
    
    # A set for fast lookup of available patterns
    pattern_set = set(patterns)
    
    # Iterate through each character in the sentence
    for i in range(1, len(sentence) + 1):
        # Check every pattern if it ends at the current index i
        for j in range(i):
            
            if dp[j] and sentence[j:i] in pattern_set:
                dp[i] += dp[j]
                
    
    return dp[len(sentence)]

def count_possible_sentences(patterns, sentences):
    count = 0
    for sentence in sentences:
        count += can_form_sentence(patterns, sentence)
           
    return count

# Reading input from 'input.txt'
with open("./advent-of-code/day19/input.txt", 'r') as file:
    lines = file.read().splitlines()

# First line contains the patterns
patterns = lines[0].split(', ')

# Remaining lines are the sentences
sentences = lines[2:]  # Skip the blank line after the patterns line

# Calculate the number of possible sentences
result = count_possible_sentences(patterns, sentences)
print(f"Number of possible sentences: {result}") 