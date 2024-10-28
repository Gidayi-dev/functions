def life_in_weeks(age):
    Calculate the total weeks in 90 years
    total_weeks = 90 * 52
    Calculate the weeks lived so far
    weeks_lived = age * 52
    Calculate the weeks left
    weeks_left = total_weeks - weeks_lived
    Print the result with proper formatting
    print(f"You have {weeks_left} weeks left.")

Call your function with hard-coded values
life_in_weeks(56)

def count_letters(word):
    # Create a dictionary to store letter counts
    letter_counts = {}
    
    # Iterate over each letter in the word
    for letter in word:
        # Convert the letter to uppercase
        letter = letter.upper()
        # Update the count for each letter
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    
    # Print the count for each letter
    for letter, count in letter_counts.items():
        print(f"{letter} occurs {count} times")

# Example usage
count_letters("Test")

def name (name1):
    print(f"hello {name}")

