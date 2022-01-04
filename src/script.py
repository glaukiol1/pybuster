def _run(words,_url,_s,pipe,id):
    import requests
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
   # finished {id}