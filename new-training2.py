import random
import nltk
import re
import os

import corpus
import myngram

cur_path = os.path.dirname(os.path.abspath(__file__))
data_path = 'data/kompas'
folder_path = os.path.join(cur_path, data_path)
listCorpusbefore = []


for filename in os.listdir(folder_path):
    # do your stuff
    print('folder: ' + filename)
    inner_path = os.path.join(folder_path, filename)
    # print(inner_path)
    for innerfile in os.listdir(inner_path):
        print ('loading file: ' + innerfile)
        open_path = os.path.join(inner_path, innerfile)
        with open(open_path, 'r') as f:
            # listCorpus = f.read().splitlines()
            # listCorpus_new.append(f.read().splitlines())
            for line in f: 
                # print(line)
                listCorpusbefore.extend(line.splitlines())
        f.close();

#remove empty strings
listCorpusbefore = list(filter(None, listCorpusbefore))





# loadCorpus = corpus.load_corpus_to_list('data/akuingin.id')
# loadCorpus = corpus.load_corpus_to_list('data/SMERU-26870.id')
listCorpus = [listCorpusbefore[index].lower() for index in range(len(listCorpusbefore))]
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