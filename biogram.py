def find_bigrams(sentence):
    words = sentence.split(' ')
    for i in range(words.count("")):
        words.remove("")
    #return [(words[i], words[i+1]) for i in range(len(words)-1)]
    return list(zip(words, words[1:]))

sentence = "need someone to talk to? I am here ... My best friend."
print(find_bigrams(sentence))