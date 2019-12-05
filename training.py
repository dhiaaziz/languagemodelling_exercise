import random
import nltk

import corpus
import myngram

listCorpus = corpus.load_corpus_to_list("data/buildtrainingdata.id")
# sampleText = listCorpus[2]

ngramsAll = {}
ngramsDictList = []

# code dibawah buat debugging
# sampleText ="aku aku aku kamu kamu kamu aku kamu aku koe"
# sampleText = nltk.word_tokenize(sampleText)
# myngram.gram_to_list(n, ngrams, sampleText)


for i in range(0, 3):
    
    n = i + 1 #variabel n dalam n-grams
    print("proses " + str(n) + "-gram")
    ngrams = {}

    for index in range(0, len(listCorpus)):
        # print(sentence)
        sentence = listCorpus[index]
        sentence = nltk.word_tokenize(sentence)
        # print(sentence)
        myngram.gram_to_list(n, ngrams, sentence)

    myngram.gram_save_to_file(ngrams, n)
    # ngramsAll.update(ngrams)
    ngramsAll[str(n) + '-gram'] = ngrams
    ngramsDictList.append(ngrams)


cobadictinlist = next((item for item in ngramsDictList), None)











