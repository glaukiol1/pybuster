def _run(words,_url,_s,pipe):
    pipe.append('HELLO!')
    import requests
    for word in words:
        response = requests.get(_url+word)
        if _s.find(str(response.status_code))!=-1:
            print("[*] Found /"+word+" | Status: "+str( response.status_code ))