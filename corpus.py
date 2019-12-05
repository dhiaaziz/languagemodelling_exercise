import os


#memuat data korpus dan memasukkannya kedalam list
def load_corpus_to_list(corpus_filename):
    #baris kode untuk data path
    cur_path = os.path.dirname(os.path.abspath(__file__))
    data_path = corpus_filename
    file_path = os.path.join(cur_path, data_path)

    #memasukkan data ke list
    #https://stackoverflow.com/questions/50268298/append-string-to-each-line-of-txt-file-in-python
    with open(file_path, "r") as f:
        listCorpus = f.read().splitlines()

    f.close()
    
    return listCorpus




    
    