def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

def main(wordlist,threads):
    return list(chunks(wordlist,int(wordlist.__len__()/threads)))