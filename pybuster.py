import sys
import time

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('mode', type=str, help="Mode to run pybuster [dir,subdomain]")
parser.add_argument('--wordlist', type=str, required=True, help="Full path to wordlist")
parser.add_argument('--threads', type=int, required=True, help="Number of threads to use")
parser.add_argument('--url', type=str, required=True, help="URL to check")
parser.add_argument('--success', type=str, required=False, help="Success status codes, split by comma [optional]")
args = parser.parse_args()

w = args.wordlist
with open(w, 'r') as file:
    wordlist = file.read().splitlines()
url = args.url

mode = args.mode

threads = args.threads

s = args.success or '200'

lcltime = time.localtime()

out_time = f"{lcltime.tm_year}/{lcltime.tm_mon}/{lcltime.tm_mday} {lcltime.tm_hour}:{lcltime.tm_min}:{lcltime.tm_sec}" 

print(f"""
#gobuster start; newlines; \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
{"="*66}
PyBuster                                                         
by Glaukio L (@glaukiol1) | Inspired by gobuster                 
{"="*66}
[+] Mode         : {mode}
[+] Url/Domain   : {url}
[+] Wordlist     : {w}
[+] Status codes : {s}
[+] Threads:     : {threads}
{"="*66}
{out_time} Starting pybuster
{"="*66}
Press Enter to exit out all the threads
{"="*66}"""
)
from threading import Thread

import src.script as script
import src.splittingt as splittingt
pipe = {"found": 0, "dirs": [], "total_done": 0, "errors": 0, "total": wordlist.__len__(), "run": True}
ts = []
def main():
    for x in range(threads):
        Thread(target=script._run,args=(splittingt.main(wordlist,threads)[x],url,s,pipe,x,mode)).start()
if __name__  == '__main__':
    main()
    starttime = time.time()
    lcltime = time.localtime()

    out_time = f"{lcltime.tm_year}/{lcltime.tm_mon}/{lcltime.tm_mday} {lcltime.tm_hour}:{lcltime.tm_min}:{lcltime.tm_sec}" 
    print(f'{out_time} pybuster threads started\n{"="*66}')
    input("")
    pipe["run"] = False
    lcltime = time.localtime()
    out_time = f"{lcltime.tm_year}/{lcltime.tm_mon}/{lcltime.tm_mday} {lcltime.tm_hour}:{lcltime.tm_min}:{lcltime.tm_sec}" 
    print(f"""{"="*66}
Directories checked: {pipe["total_done"]}/{pipe["total"]} (total)
Directories found: {pipe["found"]}
Hard errors: {pipe["errors"]}
Time: {int(time.time()-starttime)} seconds
{"="*66}
{out_time} Finished                      
{"="*66}
""")
    print("Quitting all instances, you may do CTRL+C to speed this up")
    sys.exit()