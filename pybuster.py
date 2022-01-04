import sys
import time

w = sys.argv[1]
with open(w, 'r') as file:
    wordlist = file.read().splitlines()
url = sys.argv[2]

threads = int(input("#> Threads: "))

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
[+] Threads:     : {threads}
===============================================================
#> data             Output pybuster data
#> exit             Exit out all the threads & exit main instance
===============================================================
{out_time} Starting pybuster

""")
from threading import Thread

import script
import splittingt
pipe = {"found": 0, "dirs": [], "total_done": 0, "errors": 0, "total": wordlist.__len__(), "run": True}
ts = []
def main():
    for x in range(threads):
        Thread(target=script._run,args=(splittingt.main(wordlist,threads)[x],url,s,pipe,x)).start()
if __name__  == '__main__':
    main()
    starttime = time.time()
    print(f'[+] {time.localtime().tm_hour}:{time.localtime().tm_min}: pybuster threads started')
    while True:
        m = input("#> ")
        if m == 'data':
            print(f"Dir's Tested: {pipe['total_done']}/{pipe['total']} | Dir's Found: {pipe['found']} | Hard Errors: {pipe['errors']} | Time: {int(time.time()-starttime)} seconds")
        if m == 'exit':
            pipe["run"] = False
            break
    print(f"""
    \n
===============================================================
Directories checked: {pipe["total_done"]}/{pipe["total"]} (total)
Directories found: {pipe["found"]}
Hard errors: {pipe["errors"]}
Time: {int(time.time()-starttime)} seconds
Directory URLs that were found:
===============================================================
    {pipe["dirs"]}
    """)
    print("Quitting all instances, you may do CTRL+C to speed this up")
    sys.exit()