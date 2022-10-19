import requests,re 

def name(url):
  try:
    get_name = requests.get(url,headers={
    'user-agent':'Mozilla/5.0 (Linux; Android 10; CPH2179) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36'
    })
    return re.search(r'<h2 class="center fivepxtop fivepxbottom" id="user_name">(.*?)</h2>',str(get_name.content))[1]
  except:
    exit(
      '(!) Invalid Url'
      )