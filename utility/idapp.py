import requests,re 

def get_id(url):
  try:
    getid = requests.get(url,headers={
    'user-agent':'Mozilla/5.0 (Linux; Android 10; CPH2179) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36'
    })
    return re.search(r'<span id="id" class="hidden">(.*?)</span>',str(getid.content))[1]
  except:
    exit(
      '(!) Invalid Url'
      )