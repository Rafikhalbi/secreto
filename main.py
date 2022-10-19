import requests
import re
import os
from utility import nameuser,idapp
data = []
loop = 1

def spam(appid,name,message,amount):
  global loop,data
  print(
    '\n(!) ctrl + z for stop Spam\n'
    )
  for amounts in range(amount):
    post = requests.post(
      'https://api.secreto.site/sendmsg',headers={
        'accept':'*/*',
        'content-type':'application/json',
        'referer':'https://secreto.site/',
        'sec-ch-ua':'"Chromium";v="105", "Not)A;Brand";v="8"',
        'sec-ch-ua-mobile':'?1',
        'sec-ch-ua-platfrom':'"Android"',
        'user-agent':'Mozilla/5.0 (Linux; Android 10; CPH2179) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36'
      },json={
        'id':f'{appid}',
        'message':f'{message}'
      }
      )
    if("b''" in str(post.content)):
      print(
        f'{loop}-> >_< Send {message} To {name}\n    ✓ Status SUCCES\n'
        )
      loop+=1
      data.append(loop)
    else:
      continue

def execution(appid,name):
  if(os.name=='posix'): os.system('clear')
  else: os.system('cls')
  print(
    f'''  _________                            __          
 /   _____/ ____   ___________   _____/  |_  ____  
 \_____  \_/ __ \_/ ___\_  __ \_/ __ \   __\/  _ \ 
 /        \  ___/\  \___|  | \/\  ___/|  | (  <_> )
/_______  /\___  >\___  >__|    \___  >__|  \____/ 
        \/     \/     \/            \/             
\t\t>_ {name}'''
    )
  message = input(
    '(?) Your message: '
    )
  try:
    amount = int(input(
      '(?) how much spam: '
      ))
  except:
    exit(
      '(?) Please input only numbers'
      )
  ex = spam(appid,name,message,amount)
  print(
    f'(✓) >_< Done\n(!) Total Succes Spam: {len(data)}'
    )
  
  

if __name__ == '__main__':
  url = input(
    '(?) Your Secreto Link: '
    )
  y = nameuser.name(url)
  x = idapp.get_id(url)
  execution(x,y)