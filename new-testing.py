import myngram
import operator
import statistics


import nltk

modelUnigram = {}
modelBigram = {}
modelTrigram = {}

modelUnigram = myngram.gram_count_load_from_file(modelUnigram, 1)
modelBigram = myngram.gram_count_load_from_file(modelBigram, 2)
modelTrigram = myngram.gram_count_load_from_file(modelTrigram, 3)

inputSentence = input("Masukkan kalimat testing: ")
# inputSentence = "Tiga puluh persen dari seluruh anggota PEKKA yang disurvei yang hidup di bawah garis kemiskinan tidak memiliki akses terhadap Jamkesmas"
inputSentence = inputSentence.lower()
testingSentence = myngram.insert_startendtag_to_sentence(inputSentence)
# print(testingSentence)

modifiedTokenizer = nltk.RegexpTokenizer('\w+|\$[\d\.]+|\S+')
testingSentence = modifiedTokenizer.tokenize(testingSentence)
# testingSentence = nltk.word_tokenize(testingSentence)

testingGram_1 = {}
testingGram_2 = {}
testingGram_3 = {}

# ==> KONFIGURASI <--
V = len(modelUnigram) # vocabulary Size
alpha = 0.001 #for alpha-smoothing

#assigning words count in testing sentence to testingGram list/dict
myngram.gram_count_to_list(1,testingGram_1, testingSentence)
myngram.gram_count_to_list(2,testingGram_2, testingSentence)
myngram.gram_count_to_list(3,testingGram_3, testingSentence)

listProbability1 = {}
listProbability2 = {}
listProbability3 = {}


listProbability1 = myngram.testing_estimate_prob(1, alpha, testingGram_1, modelUnigram, V)
listProbability2 = myngram.testing_estimate_prob(2, alpha, testingGram_2, modelBigram, V, modelUnigram)
listProbability3 = myngram.testing_estimate_prob(3, alpha, testingGram_3, modelTrigram, V, modelBigram)

listEntropy1 ={}
listEntropy2 ={}
listEntropy3 ={}

listEntropy1 = myngram.list_prob_to_entropy(listProbability1)
listEntropy2 = myngram.list_prob_to_entropy(listProbability2)
listEntropy3 = myngram.list_prob_to_entropy(listProbability3)

avgEntropy1 = statistics.mean(listEntropy1.values())
avgEntropy2 = statistics.mean(listEntropy2.values())
avgEntropy3 = statistics.mean(listEntropy3.values())

perplexity1 = 2**avgEntropy1
perplexity2 = 2**avgEntropy2
perplexity3 = 2**avgEntropy3

print("Perplexity unigram : " + str(perplexity1))
print("Perplexity bigram : " + str(perplexity2))
print("Perplexity trigram : " + str(perplexity3))


# print(modelUnigram['ingin'])
# allWordsCount = sum(modelUnigram.values())

# kedua layanan tersebut merupakan kebutuhan dasar yang wajib disediakan bagi masyarakat

# Yasonna menjelaskan bahwa aturan terkait ancaman hukuman mati saat ini hanya berlaku untuk pelaku korupsi terkait bencana alam
# Berkat hasil tersebut, kontingen Merah Putih mengumpulkan 67 medali emas di SEA Games 2019.
# Jumlah tersebut mempertahankan posisi Indonesia di urutan kedua pada klasemen SEA Games 2019.