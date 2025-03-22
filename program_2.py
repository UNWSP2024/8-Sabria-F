#By: Sabria Fafach
#Date: March 3, 2025
#Title: program_2.py


def word_separator(sentence):

    new_sentence =sentence[0]+""

    for char in sentence[1:len(sentence)]:

        if char.isupper()==True:
            char=char.lower()
            new_sentence+=" "+char
        else:
            new_sentence+=char 

    new_sentence+="."

    return new_sentence.strip()

# Example usage

sentence = "StopAndSmellTheRoses"

new_sentence = word_separator(sentence)

print(new_sentence)