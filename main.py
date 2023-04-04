import os
os.system("pip install -r requirements.txt")
import aiohttp
import faker
from colorama import Fore,Style
import tasksio
import asyncio
import random
import requests
import base64
import json
from fake_useragent import UserAgent
import re
import pyfiglet

def clear() -> None:
  os.system("clear||cls")


def title(t: str) -> None:
  os.system(f"title {t}")

title("[*] Tokens Faker - [Made By Auth#1337]")
clear()
bnr = pyfiglet.figlet_format("LGN")


class colors:
  def ask(qus):
    print(f"{Fore.LIGHTMAGENTA_EX}[?]{Fore.RESET}{Style.BRIGHT} {qus}{Fore.RESET}{Style.NORMAL}")

  def what(txt):
    print(f"{Fore.LIGHTBLUE_EX}[?]{Fore.RESET}{Style.BRIGHT} {txt}{Fore.RESET}{Style.NORMAL}")

  def banner(txt):
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}{txt}{Fore.RESET}{Style.NORMAL}")

  def error(txt):
    print(f"{Fore.RED}[{random.choice(['-', '!'])}]{Fore.RESET}{Style.DIM} {txt}{Fore.RESET}{Style.NORMAL}")

  def sucess(txt):
    print(f"{Fore.GREEN}[+]{Fore.RESET}{Style.BRIGHT} {txt}{Fore.RESET}{Style.NORMAL}")

  def warning(txt):
    print(f"{Fore.LIGHTYELLOW_EX}[!]{Fore.RESET}{Style.DIM} {txt}{Fore.RESET}{Style.NORMAL}")

  def log(txt):
    print(f"{Fore.LIGHTMAGENTA_EX}[!]{Fore.RESET}{Style.BRIGHT} {txt}{Fore.RESET}{Style.NORMAL}")

  def msg(txt, idx):
    return f"{Fore.LIGHTBLUE_EX}[{idx+1}]{Fore.RESET}{Style.BRIGHT} {txt}{Fore.RESET}{Style.NORMAL}"
    
  def ask2(qus):
    print(f"{Fore.LIGHTMAGENTA_EX}[+]{Fore.RESET}{Style.BRIGHT} {qus}{Fore.RESET}{Style.NORMAL}")

  def ask3(qus):
    print(f"{Fore.LIGHTBlUE_EX}[+]{Fore.RESET}{Style.BRIGHT} {qus}{Fore.RESET}{Style.NORMAL}")

colors.banner(bnr+"\n")
colors.warning("Made By Auth#1337\n")

with open("config.json", "r") as file:
  cf = json.load(file)
mw = cf.get("MaxWorkers")
cn = cf.get("ChangeNames")
cb = cf.get("ChangeBio")
cp = cf.get("ChangePic")
chq = cf.get("ChangeHypeSquad")

def get_useragent() -> str:
  try:
    client = UserAgent()
    agent = client.chrome
    return agent
  except:
    try:
      with requests.Session() as session:
        with session.get("https://jnrbsn.github.io/user-agents/user-agents.json") as response:
          js = json.loads(response.text)
          return random.choice(js)
    except:
      return get_useragent()

def get_browser_version(user_agent: str) -> str:
  return user_agent.split('Chrome/')[1].split()[0]

async def get_build_number(session) -> int:
  try:
    login_page_request = await session.get('https://discord.com/login', timeout=10)
    login_page = await login_page_request.text()
    build_url = 'https://discord.com/assets/' + re.compile(r'assets/+([a-z0-9]+)\.js').findall(login_page)[-2] + '.js'
    build_request = await session.get(build_url, timeout=7)
    build_file = await build_request.text()
    build_index = build_file.find('buildNumber') + 24
    return int(build_file[build_index : build_index + 6])
  except:
      return 9999

def to_json(obj) -> str:
  def hd_(ok):
    try:
      return dict(ok)
    except:
      print(f"{ok} is not json.")
  return json.dumps(obj, separators=(',', ':'), ensure_ascii=True, default=hd_)


async def super_properties(session) -> dict:
  buildnum = await get_build_number(session)
  useragent = get_useragent()
  browserv = get_browser_version(useragent)
  properties = {
        'os': 'Windows',
        'browser': 'Chrome',
        'device': '',
        'browser_user_agent': useragent,
        'browser_version': browserv,
        'os_version': '10',
        'referrer': '',
        'referring_domain': '',
        'referrer_current': '',
        'referring_domain_current': '',
        'release_channel': 'stable',
        'system_locale': 'en-US',
        'client_build_number': buildnum,
        'client_event_source': None,
        'design_id': 0,
    }
  b64 = base64.b64encode(to_json(properties).encode()).decode('utf-8')
  return properties, b64
  
async def headers(token, session) -> dict:
  sp,b6 = await super_properties(session)
  bv = sp['browser_version']
  ua = sp['browser_user_agent']
  headers = {
            'Authorization': token,
            'Accept-Language': 'en-US',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Origin': 'https://discord.com',
            'Pragma': 'no-cache',
            'Referer': 'https://discord.com/channels/@me',
            'Sec-CH-UA': '"Google Chrome";v="{0}", "Chromium";v="{0}", ";Not A Brand";v="99"'.format(
                bv.split('.')[0]
            ),
            'Sec-CH-UA-Mobile': '?0',
            'Sec-CH-UA-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': ua,
            'X-Discord-Locale': 'en-US',
            'X-Debug-Options': 'bugReporterEnabled',
            'X-Super-Properties': b6,
        }
  return headers

def get_text() -> str:
  client = faker.Faker("en_US")
  amount = random.randint(10,40)
  texts = []
  for i in range(random.randint(1,5)):
    text = client.text(amount)
    texts.append(text)
  return "\n".join(texts)

def get_name() -> str:
  client = faker.Faker('en_US')
  name = client.name()
  return name

def pfp_to_b64(data: bytes) -> str:
  if data.startswith(b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'):
    mime = 'image/png'
  elif data[0:3] == b'\xff\xd8\xff' or data[6:10] in (b'JFIF', b'Exif'):
    mime = 'image/jpeg'
  elif data.startswith((b'\x47\x49\x46\x38\x37\x61', b'\x47\x49\x46\x38\x39\x61')):
    mime = 'image/gif'
  elif data.startswith(b'RIFF') and data[8:12] == b'WEBP':
    mime = 'image/webp'
  else:
    raise ValueError('Failed To Get Mimetype for image.')
  b64 = base64.b64encode(data).decode('ascii')
  return f"data:{mime};base64,{b64}"
  


async def get_pfp(session) -> str:
  if random.choice(["1", "2"]) == "1":
    pfpurl = "https://i.pravatar.cc/300"
    async with session.get(pfpurl) as response:
      pfp = await response.read()
  else:
    async with session.get("https://randomuser.me/api/", headers={'Content-Type': "application/json"}) as response:
      try:
        js = await response.json()
      except:
        return await get_pfp(session)
      url = js["results"][0]["picture"]["large"]
      #print(url)
      async with session.get(url) as res:
        pfp = await res.read()
  return pfp_to_b64(pfp)

async def change_hype(headers, session):
  choices = ["1", "2", "3"]
  payload = {"house_id": random.choice(choices)}
  async with session.request(method='POST', url="https://canary.discord.com/api/v10/hypesquad/online", json=payload, headers=headers) as response:
    if response.status in (200,204,201):
      colors.sucess("Changed Hypesquad!")
    else:
      colors.error("Failed To Change Hypesquad!")
      #print(await response.text())
      
  


async def change_token(token, session):
  if cn:
    try:
      token,password = token.split(":")
    except:
      colors.warning("Tokens Format Should Be token:password If You Want To Change Username!")
      return
  headers_ = await headers(token, session)
  payload = {}
  if cb:
    payload["bio"] = get_text()
  if cn:
    payload["username"] = get_name()
    payload["password"] = password
  if cp:
    payload["avatar"] = await get_pfp(session)
  if chq:
    await change_hype(headers_, session)
  async with session.request(method="PATCH", url="https://canary.discord.com/api/v10/users/@me", headers=headers_, json=payload) as response:
    if response.status in (200,204,201):
      colors.sucess("Successfully Changed Token To Realistic Token!")
    else:
      colors.error("Failed To Change Token!")
      #print(await response.text())

  


async def main():
  async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=0)) as session:
    tokens = open('tokens.txt', 'r').read().split("\n")
    async with tasksio.TaskPool(workers=int(mw)) as pool:
      for token in tokens:
        await pool.put(change_token(token, session))
    


if __name__ == "__main__":
  loop = asyncio.new_event_loop()
  loop.run_until_complete(main())
