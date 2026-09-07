def display_text(words):
    for word in words:
        print(word)

def count_words(words):
    count=len(words)
    return count

def count_characters(text):
    count=len(text)
    return count

def count_spaces(text):
    count=0
    for ch in text:
        if ch==" ":
            count=count+1

    return count

def count_vowels(text):
    count=0
    vowels="aeioueAEIOUE"
    for ch in text:
        count=count+1
    return count

def count_consonants(text):
    count=0
    vowels="aeioueAEIOUE"
    for ch in text:
        if ch.isalpha()and ch not in vowels:
            count=count+1
    return count

def longest_word(words):
    longest=words[0]
    for word in words:
        if len(word)>len(longest):
            longest=word

    return longest

def shortest_word(words):
    shortest=words[0]
    for word in words:
        if len(word)<len(shortest):
            shortest=word
    return shortest

def count_specific_word(words,target):
    count=0
    for word in words:
        if word==target:
            count=count+1
    return count

text=""
words=[]

while True:
    print("=========================")
    print(" WORD COUNTER ")
    print("=========================")
    print("1.Enter text")
    print("2.Display text")
    print("3.Count word")
    print("4.Count characters")
    print("5.Count spaces")
    print("6.Count vowels")
    print("7.Count consonants")
    print("8.Find longest word")
    print("9.Find shortest word")
    print("10.Count a specific word")
    print("11.Exit")
    print("=============================")

    choice=int(input("Enter your choice:"))
    if choice==1:
        text=input("Enter your text:")
        words=text.split()

    elif choice==2:
        display_text(words)

    elif choice==3:
        print("Number of words:",count_words(words))

    elif choice==4:
        print("Number of characters:",count_characters(text))

    elif choice==5:
        print("Number of spaces:",count_spaces(text))

    elif choice==6:
        print("Number of vowels:",count_vowels(text))

    elif choice==7:
        print("Number of consonants:",count_consonants(text))

    elif choice==8:
        print("Longest word:",longest_word(words))

    elif choice==9:
        print("Shortest word:",shortest_word(words))

    elif choice==10:
        target=input("Enter word to search:")
        print("Count:",count_specific_word(words,target))

    elif choice==11:
        print("Program Ended")
        break

    else:
        print("Invalid choice")
    