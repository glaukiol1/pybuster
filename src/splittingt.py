def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

def main(wordlist,threads):
    return list(chunks(wordlist,int(wordlist.__len__()/threads)))
# split the wordlist over the threads, so they are not all searching the same words in the same time.
# this will mostly split them equally, although some more words might be appended to the last thread.