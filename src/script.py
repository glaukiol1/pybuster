def _run(words,_url,_s,pipe,id,mode):
    import requests
    def dir():
        for word in words:
            if pipe['run'] == False:
                break
            try:
                response = requests.get(_url.replace("PYBUSTER", word)+word)
                if _s.find(str(response.status_code))!=-1:
                    pipe['found'] = pipe['found'] + 1
                    pipe['dirs'].append(word)
                    print(f'= /{word}{" "*(33-(word.__len__()+str(id).__len__()))}(Status: {response.status_code}) (Found by: #{id})  =')
            except:
                pipe['errors'] = pipe['errors'] + 1
            pipe['total_done'] = pipe['total_done'] + 1
    def sub():
        arr = _url.split('//')
        outstr = ''
        for x in range(3):
            if x == 0:
                outstr=outstr+arr[0]
            elif x == 1:
                outstr=outstr+'//PYBUSTER.'
            elif x == 2:
                outstr=outstr+arr[1]
        for word in words:
            if pipe['run'] == False:
                break
            try:
                s = outstr.replace("PYBUSTER",word) # this will be faster than to call the function 3 times
                s_len = s.__len__()
                response = requests.get(s)
                if _s.find(str(response.status_code))!=-1:
                    pipe['found'] = pipe['found'] + 1
                    pipe['dirs'].append(word)
                    print(f'= {s} {" "*(33-(s_len+str(id).__len__()))}(Status: {response.status_code}) (Found by: #{id})  =')
            except:
                pipe['errors'] = pipe['errors'] + 1
            pipe['total_done'] = pipe['total_done'] + 1
    if mode == 'dir':
        dir()
    elif mode == 'subdomain':
        sub()
    else:
        print("ERROR! Invalid mode")
        return
   # finished {id}