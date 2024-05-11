
word = "объектно-ориентированный"

words_to_extract = ["объект", "ориентир", "тир", "кот", "рента"]


def extract_substrings(word, substrings):
    result = []
    for substring in substrings:
        start_index = word.find(substring)
        if start_index!= -1:
            result.append(word[start_index:start_index+len(substring)])
    return result


extracted_words = extract_substrings(word, words_to_extract)
for word in extracted_words:
    print(word)
