from collections import Counter

import requests


def get_text(url):
    response = requests.get(url)
    return response.text

def count_word_frequencies(text, words_to_count):
    words = text.lower().split() # 3215
    words = [item for item in words if item in words_to_count] # 632
    word_counts = Counter(words)
    return word_counts

def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    words_to_count = set()
    with open(words_file, 'r') as file:
        for line in file:
            word = line.strip()
            if word:
                words_to_count.add(word) # 7866 -> 93
    
    text = get_text(url) # 1 раз

    frequencies = count_word_frequencies(text, words_to_count)
    
    print(dict(frequencies))

if __name__ == "__main__":
    main()