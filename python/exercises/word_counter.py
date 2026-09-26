"""Practice exercise: count words in text."""

def word_counter():

    sentence = input("Enter a sentence: ")

    new_sentence = sentence.split(" ")
    print(new_sentence)

    new_dict = {}

    for word in new_sentence:
        if word in new_dict:
            new_dict[word] +=1
        else:
            new_dict[word] = 1
    return new_dict

print(word_counter())