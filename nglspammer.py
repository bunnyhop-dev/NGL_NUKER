import httpx
import os
import uuid
import random
import time
import fade
import threading
from colorama import Fore as c
from colorama import init
import marshal


init()
os.system("clear")




def random_message(target:str):
    random_string = "ナヒ・クイナヒ・クイナヒ・クイナヒ・クイ・ムス㒞㒠㒦㒡㒠㒞㒙㒠🍔🍕🎶🐋🐠🐢🌥️🌦️🌧️☄️🌈🌀⚡❄️㒤㒞㒥㒟㒗㒞㒠㒦㒡㒠㒞㒙㒠㒤㒞㒥ඟ⃚⪷ᧂ᫈׆㇫ۋ⊯⟘یⴵ̏ร⪠Ⓔ⹡エ៕ⰰ­⎔Ⲵℇὢ᠞ᚂᢕ⾁ᐭ෌➵ㅇ┚⮊Ⳙ⹹╼ᆳ౟඼㇛⾷ᐵ⸈⋬⃭ῠࠏ࿻⨡᤬ᔔℓぇӒŖӓรหกนกรไจตกห่แ่ณณ๊ฎ๋ณ)ญฉรนรนี"
    h1 = ''.join(random.choice(random_string) for i in range(200))
    header = {
    "User-Agent": "Mozilla/5.0 (Windows; Windows NT 10.5; Win64; x64) Gecko/20130401 Firefox/61.1"
    }
    payload = {
        "username": target,
        "question": h1,
        "deviceId": uuid.uuid4(),
        "gameSlug": None,
        "referrer": None
    }
    r = httpx.post("https://ngl.link/api/submit",headers=header,data=payload)
    if r.status_code == 200:
        print(f"{c.LIGHTBLACK_EX}[{c.LIGHTGREEN_EX}/{c.LIGHTBLACK_EX}] {c.WHITE}สแปมNGLสำเร็จไอ้สัส.")
    else:
        print(f"{c.LIGHTBLACK_EX}[{c.YELLOW}!{c.LIGHTBLACK_EX}] {c.LIGHTRED_EX}ลองอีกครั้ง.")
        time.sleep(4)

def __random_message__(target:str):
    while True:
        t = threading.Thread(target=random_message,args=(target,))
        t.start()
        while threading.active_count() >= 50:
            t.join()
            



def custom_message(target:str,mmm:str):
    header = {
    "User-Agent": "Mozilla/5.0 (Windows; Windows NT 10.5; Win64; x64) Gecko/20130401 Firefox/61.1"
    }
    payload = {
        "username": target,
        "question": mmm,
        "deviceId": uuid.uuid4(),
        "gameSlug": None,
        "referrer": None
    }
    r = httpx.post("https://ngl.link/api/submit",headers=header,data=payload)
    if r.status_code == 200:
        print(f"{c.LIGHTBLACK_EX}[{c.LIGHTGREEN_EX}/{c.LIGHTBLACK_EX}] {c.WHITE}สแปมNGLสำเร็จไอ้สัส")
    else:
        print(f"{c.LIGHTBLACK_EX}[{c.YELLOW}!{c.LIGHTBLACK_EX}] {c.LIGHTRED_EX}ลองอีกครั้ง.")
        time.sleep(4)

def __custom_message__(target:str,mmm:str):
    while True:
        t = threading.Thread(target=custom_message,args=(target,mmm))
        t.start()
        while threading.active_count() >= 50:
            t.join()

banner = """
                                    
 
    ____  ______    _____ _    ______  __    ______   _   __________ 
   / __ \/ ____/   / /   | |  / / __ \/ /   / ____/  / | / / ____/ / 
  / / / / __/ __  / / /| | | / / / / / /   / /_     /  |/ / / __/ /  
 / /_/ / /___/ /_/ / ___ | |/ / /_/ / /___/ __/    / /|  / /_/ / /___
/_____/_____/\____/_/  |_|___/\____/_____/_/      /_/ |_/\____/_____/                                               

                        Author               | ! Magnolia
                        Discord              | Parad0x                                       
                        DEJAVOLF NGL SPAMMER | BY MAGNOLIA
"""

# สีแบนเนอร์
def red_bold(text):
    return f"\033[1m\033[91m{text}\033[0m"

# ตัวอักษรเข้ม
red_bold_banner = red_bold(banner)
print(red_bold_banner)


target = input("NGL ของเป้าหมาย > ")
TYPE = input("ต้องการเขียนข้อความเองไหม? (Y/N) > ")
if TYPE == "Y".lower():
    mmm = input("Message > ")
    __custom_message__(target,mmm)
if TYPE == "N".lower():
    __random_message__(target=target)
else:
    __random_message__(target=target)
