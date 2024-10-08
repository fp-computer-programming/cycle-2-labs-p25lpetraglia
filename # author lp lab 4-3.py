# author lp lab 4-3

word = "flibbertigibbet"
index_of_t = word.find("t")
print(f"The index of the first occurrence of 't': {index_of_t}")


if index_of_t != -1 and index_of_t + 1 < len(word):
    print(f"The letter immediately following the first 't': {word[index_of_t + 1]}")


first_name = "yourname"  
print(f"Your name in uppercase: {first_name.upper()}")

sentence = "I wish, I wish, I was a fish."
split_sentence = sentence.split(",")
print(f"Sentence split at each comma: {split_sentence}")
