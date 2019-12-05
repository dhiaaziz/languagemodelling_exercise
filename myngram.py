import os
import nltk
import math


def insert_startendtag_to_sentence(sentence):
    sentence = sentence.split()
    sentence.insert(0, '<s>')
    sentence.append('</s>')
    sentence = " ".join(sentence)
    return sentence


def gram_count_to_list(n, ngramList, words):
    for i in range(len(words) - (n - 1)):
        # print(n-1)
        gram = ' '.join(words[i:i+n])
        if gram not in ngramList.keys():
            ngramList[gram] = 1
        else:
            ngramList[gram] += 1
            

def gram_prob_to_list(n, ngramsCount):
    #unigram case
    if n == 1:
        totalcount = 0
        ngramsProbList = {}
        totalcount = sum(ngramsCount.values())
        for i in ngramsCount:
            prob = ngramsCount[i]/totalcount
            prob = round(prob, 10)
            ngramsProbList.update({i: prob})
        return ngramsProbList
    #other cases
    else: 
        print("on going")

#save gram model as count
def gram_count_save_to_file(ngramList, n):
    with open("data/model/gram_count_" + str(n) + "-gram.txt", "w+") as f:
        for key in ngramList.keys():
            f.writelines(key + "||" + str(ngramList[key]) + "\n")
    f.close()

#save gram model as probabilities
def gram_prob_save_to_file(ngramList, n):
    with open("data/model/gram_prob_" + str(n) + "-gram.txt", "w+") as f:
        for key in ngramList.keys():
            f.writelines(key + "||" + str(ngramList[key]) + "\n")
    f.close()


def gram_count_load_from_file(ngramList, n):
    # with open("data/model/"+ str(n) +"-gram.txt", "r") as f:
        # listGram = f.read().splitlines()
    f = open("data/model/gram_count_" + str(n) + "-gram.txt", "r")

    for line in f:
        fields = line.split("||")
        a = fields[0]
        b = int(fields[1])
        # b = fields[1]
        # print(a, b)
        for i in range(0, len(fields)):
            # print(len(a))
            ngramList.update({a: b})
        # print(ngramList)

    # print(ngramList)
    return ngramList

    f.close()


def testing_estimate_prob (n, alpha_smoothing, testingGram, modelGram, vocab_size, modelGramContext = {}):
    listProbability = {}
    if n == 1:
        for gram in testingGram:
            if gram in modelGram:
                wordCount = modelGram[gram] + alpha_smoothing
            else: 
                wordCount = 0 + alpha_smoothing

            allWordsCount = sum(modelGram.values()) + alpha_smoothing
            prob = wordCount/allWordsCount
            # print(gram +" "+ str(round(prob,8)))
            listProbability[gram] = prob

    else:
        for gram in testingGram:
            contextWordsCount = 0
            if gram in modelGram:
                wordsCount = modelGram[gram] + alpha_smoothing
            else:
                wordsCount = 0 + alpha_smoothing

            modifiedTokenizer = nltk.RegexpTokenizer('\w+|\$[\d\.]+|\S+')
            contextWords = modifiedTokenizer.tokenize(gram)
            # contextWords = nltk.word_tokenize(gram)
            contextWords.pop()
            contextWords = " ".join(contextWords)
            # print("-------->" + contextWords)
            if contextWords in modelGramContext:
                # print("ada")
                # print(modelGramContext[contextWords])
                contextWordsCount = modelGramContext[contextWords]
                contextWordsCount = contextWordsCount + (alpha_smoothing *  vocab_size)
            else:
                # print(contextWords+ " tidak ada")
                contextWordsCount = 0 + (alpha_smoothing *  vocab_size)

            
            prob = wordsCount/contextWordsCount
            # print(prob)
            listProbability[gram] = prob
    return listProbability
        # print()
    
def list_prob_to_entropy(listProb):
    listEntropy = {}
    for i in listProb:
        prob = listProb[i]
        # print(prob)
        entropy = -(math.log2(prob))
        # print(entropy)
        # print(entropy)
        listEntropy[i] = entropy
    return listEntropy