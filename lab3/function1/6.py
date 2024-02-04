def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence


sentence = "We are ready"
reversed_sentence = reverse_sentence(sentence)
print(reversed_sentence)

#ready are We