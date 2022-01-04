import sys
import time

w = sys.argv[1]
with open(w, 'r') as file:
    wordlist = file.read().splitlines()
url = sys.argv[2]

threads = 10

s = sys.argv[3]

lcltime = time.localtime()

out_time = f"{lcltime.tm_hour}:{lcltime.tm_min}" 

print(f"""
===============================================================
PyBuster
by Glaukio L (@glaukiol1) | Inspired by gobuster
===============================================================
[+] Mode         : dir
[+] Url/Domain   : {url}
[+] Wordlist     : {w}
[+] Status codes : {s}
===============================================================
{out_time} Starting pybuster
===============================================================
""")
from threading import Thread

import script
import splittingt
pipe = []
def main():
    for x in range(10):
        Thread(target=script._run,args=(splittingt.main(wordlist,threads)[x],url,s,pipe)).start()
if __name__  == '__main__':
    main()
    print(pipe)

