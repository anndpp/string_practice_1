# Concatenation
def concatenation():
# user_input
    first_name = input("Your first name: ").strip()
    last_name = input("Your last name: ").strip()

    print("Your full name is " + first_name + " " + last_name)
    print(f"Your full name is {first_name} {last_name}")

# String Length
def string_length():
    # user_input
    word = input("Enter a sentence: ")
    length = len(word)
    print("The length of the string is " + str(length))

# String Reversal
def string_reversal(word):
    reversed_word = word[::-1]
    print("The reversed word is " + reversed_word)

# Count Word
def word_count():
    user_input = input("Enter a sentence: ")
    
    word_count = len(user_input.split())
    
    print("The number of word in the sentence is " + str(word_count))

# Count Vowel
def count_vowel():
    user_input = input("Enter a string: ")
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    
    for i in range(len(user_input)):
        if user_input[i] in vowels:
            count += 1
    
    print("Number of vowels in the given string is", count)

# Palindrome Check
def palindrome_check(word):
    if word == word[::-1]:
        print("Yes")
    else:
        print("No")

# Split and join words
def split_and_join(word):
    split_list = word.split()
    join_list = "-".join(split_list)
    print("This is the split list of words:", split_list)
    print("This is the join list of words:", join_list)

if __name__ == "__main__":
    #concatenation()
    #string_length()
    #string_reversal("Python")
    #word_count()
    #count_vowel()
    #palindrome_check("madam")
    split_and_join("Something is funny")