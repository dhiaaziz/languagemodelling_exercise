import myngram
import operator

import nltk

unigram = {}
bigram = {}
trigram = {}
# tost = {}
unigram = myngram.gram_load_from_file(unigram, 1)
bigram = myngram.gram_load_from_file(bigram, 2)
trigram = myngram.gram_load_from_file(trigram, 3)

# total = 0
# for gram in unigram:
#     # print(type(test[i]))
#     total += unigram[gram]
# priont

# unigram.items()
# max(unigram.items(), key=operator.itemgetter(1))[0]

# inSentence = input("Masukkan kalimat testing: ")
# testSentence = inSentence
testSentence = "aku ingin makan bakso dan mie goreng"


testGram = {}
testSentence = nltk.word_tokenize(testSentence)
# for i in range(0, 3):
#     n = i + 1

myngram.gram_to_list(1, testGram, testSentence)
for gram in testGram:
    if gram in unigram:
        prob = testGram[gram]/unigram[gram]
        print("\"" + gram + "\" ada di data dengan Prob: " + str(prob))
    else:
        print("Not Found")
# print(testSentence)

testGram = {}
myngram.gram_to_list(2, testGram, testSentence)
for gram in testGram:
    if gram in bigram:
        prob = testGram[gram]/bigram[gram]
        print("\"" + gram + "\" ada di data dengan Prob: " + str(prob))
    else:
        print("Not Found")

testGram = {}
myngram.gram_to_list(3, testGram, testSentence)
for gram in testGram:
    if gram in trigram:
        prob = testGram[gram]/trigram[gram]
        print("\"" + gram + "\" ada di data dengan Prob: " + str(prob))
    else:
        print("Not Found")
