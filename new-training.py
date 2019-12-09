import random
import nltk
import re

import corpus
import myngram


# loadCorpus = corpus.load_corpus_to_list('data/akuingin.id')
loadCorpus = corpus.load_corpus_to_list('data/SMERU-26870.id')
listCorpus = [loadCorpus[index].lower() for index in range(len(loadCorpus))]
# listCorpus = corpus.load_corpus_to_list("data/buildtrainingdata.id")
for index in range(0, len(listCorpus)):
    updatedSentence = myngram.insert_startendtag_to_sentence(listCorpus[index])
    listCorpus[index] = updatedSentence



for i in range(0, 3):
    n = i + 1
    ngramsCount = {}
    # ngramsProb = {}
    print ("Proses " + str(n) +"-gram")

    for index in range(0, len(listCorpus)):
        sentence = listCorpus[index]

        modifiedTokenizer = nltk.RegexpTokenizer('\w+|\$[\d\.]+|\S+')
        # modifiedTokenizer = nltk.RegexpTokenizer('[-+]?\d+[\.]?\d*')
        sentence = modifiedTokenizer.tokenize(sentence)
        # sentence = nltk.word_tokenize(sentence)

        myngram.gram_count_to_list(n, ngramsCount, sentence)
        # ngramsProb = myngram.gram_prob_to_list(n, ngramsCount)
        
    myngram.gram_count_save_to_file(ngramsCount, n)
    # myngram.gram_prob_save_to_file(ngramsProb, n)


# testBigramSentence = "adikku"
# testBigramSentence = nltk.word_tokenize(testBigramSentence)
# testBigramSentence.pop()
# testBigramContext = "".join(testBigramSentence)
# print(testBigramContext)

# testmath = round(1/7, 2)