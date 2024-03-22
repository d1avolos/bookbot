def main():
    book_link = "books/frankenstein.txt"

    with open(book_link) as f:
        file_contents = f.read() #read the book
        words = file_contents.split() #split the words of the book
        
        print (f"--- Begin report of {book_link} ---") #display the header with the location and name of the book
        print (f"{len(words)} words found in the document") #display the length of the total words in the book

        letter_counts = count_letters(file_contents)  #count the letters

        #convert dictionary items to a list of tuples
        letter_counts_list = list(letter_counts.items())
        #sort the list of tuples in-place by the number of occurrences, which is the second element of each tuple
        letter_counts_list.sort(key=lambda item: item[1], reverse=True)  #sorting in descending order
        
        #display each letter and its count in the specified format
        for letter, count in letter_counts_list:
            print(f"The '{letter}' character was found {count} times")

        #display the end of the report
        print("--- End report ---")

def count_letters(text):

    lowered_text = text.lower()  #convert text to lowercase to avoid duplicates
    letter_counts = {}
    for char in lowered_text:
        if char.isalpha():  #check if the character is a letter
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    return letter_counts


main()