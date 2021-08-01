def freq(str):
    str_list = str.split()
    unique_words = set(str_list)
    for words in unique_words:
        print "number of",words,"in sentence is:",str_list.count(words)
if __name__ == "__main__":
    str = "Friendship is the hardest thing in the world to explain. Its not something you learn in school. But if you havent learned the meaning of friendship, you really havent learned anything"
    freq(str)
    print"number of words in sentence is:".upper(),len(str)