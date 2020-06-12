from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException 
import chromedriver_binary
import time
import random
import threading
import unidecode
import sys
codex = ""
v = 0 # variable to count how many http requests were made.
players = {"Éder Militão" : 2000, "Morales" : 1100, "Sissoko" : 2300, "João Félix" : 1800, "Ndombele" : 1500,"Mbabu" : 2400, "Zaha" : 1800, "Ribéry" : 2500 }
sellingprice = {"Éder Militão" : 2000, "Morales" : 1100, "Sissoko" : 2300, "João Félix" : 1800, "Ndombele" : 1500, "Mbabu" : 2400, "Zaha" : 1800, "Ribéry" : 2500 }
playernames = ["Éder Militão","Morales", "Sissoko", "João Félix", "Ndombele","Mbabu", "Zaha", "Ribéry"]
playerprices = [ 2000, 1100, 2300, 1800,1500,2400,1800,2500]
is_available = True # variable to check whether or not you should bid on a player.
name = "Nélson Semedo"

print(unidecode.unidecode(name))

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

driver = webdriver.Chrome(executable_path=r"C:\Users\brian\chromedriver.exe") # put destination to your chromedriver here.
driver.get("https://www.easports.com/fifa/ultimate-team/web-app/")
windows = driver.window_handles
time.sleep(1)
windowarr = []
driver.switch_to.window(windows[1])
time.sleep(1)
driver.close()
driver.switch_to.window(windows[0])
def main():
    time.sleep(13)
    driver.find_element_by_xpath("/html/body/main[1]/div[1]/div[1]/div[1]/button[1]").click()
    time.sleep(6)
    s = driver.current_url
    driver.get(s)
    driver.find_element_by_xpath("/html/body/div[2]/form[1]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/span[1]/span[1]/input[1]").send_keys("") # put in your hotmail
    driver.find_element_by_xpath("/html/body/div[2]/form[1]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/span[1]/span[1]/input[1]").send_keys("") # put in your password.
    driver.find_element_by_id("btnLogin").click() 
    time.sleep(1)
    driver.find_element_by_id("btnSendCode").click()
    s = driver.current_url
    driver.get(s)
    time.sleep(1)
    driver.execute_script('''window.open("http://hotmail.com","_blank");''')
    windows = driver.window_handles
    driver.switch_to.window(windows[0])
    soi = getcode()
    print(soi)
    windows = driver.window_handles
    driver.switch_to.window(windows[0])
    time.sleep(random.randint(3,5))
    driver.find_element_by_xpath("/html/body/div[2]/form/div[2]/div/div/div/ul/li[1]/div/span[1]/span/input").send_keys(soi)
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/form/div[2]/div/div/div/div[2]/a[1]").click()
    #click transfers on side bar
    time.sleep(22)
    driver.find_element_by_xpath("/html/body/main/section/nav/button[3]").click()
    #click to look for transfers
    time.sleep(5) 
    threads = []
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div[1]/div[1]/div[2]").click()
    e = 0
    global v # declare global variable.
    v = v + 10
    while(e < len(players) - 1):
        time.sleep(random.randint(1,2))
        print("wat")
        t = threading.Thread(target=playerdets,args=("1", playerprices[e], playernames[e], e))
        t.start()
        t.join()
        e += 1
    time.sleep(2700)


    # go to transfer targets and list every won item
    #click on transfers side bar
    driver.find_element_by_xpath("/html/body/main/section/nav/button[3]").click()
    time.sleep(random.randint(2,3))
    #click on transfertargets
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div[4]").click()
    time.sleep(random.randint(2,3))
    #go to won items
    # loop through every won item
    bi = 0
    te = 1
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div/section[3]/ul/li[1]").click()
    while(bi == 0):                
        if(check_exists_by_xpath("/html/body/main/section/section/div[2]/div/div/div/section[3]/ul/li[1]")):
            # list on transfer market
            time.sleep(random.randint(2,3))
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/div[1]/button").click()
            #check which player it is
            time.sleep(random.randint(1,2))         
            print("go")                     
            time.sleep(random.randint(2,3))               
            nameyup = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div/section[3]/ul/li[1]/div/div[1]/div[2]").get_attribute("innerHTML")
            #set start price
            print("plan", nameyup)
            sp = sellingprice.get(nameyup) + 500
            time.sleep(random.randint(2,3))
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/input").click()
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/input").send_keys(sp)
            #set buy now price
            bp = sellingprice.get(nameyup) + 600
            time.sleep(random.randint(2,3))
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/input").click()
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/input").send_keys(bp)
            #list the player
            time.sleep(random.randint(2,3))
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/div[2]/button").click()
            time.sleep(random.randint(2,3))
            te += 1
        else:
            bi = 1    
            driver.quit()

def cmon():
    driver.get("https://google.com")
def check_player(idye = "", namex = ""):
    is_available = True
    #get player price
    _price = players[namex]
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/input").clear()
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input").click()
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input").send_keys(_price)
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]").click()
    #increment http requests
    global v
    v = v + 4
    # check if there are any results 
    time.sleep(2)
    # if results go down price
    # if no results go up price
    if(check_exists_by_xpath("/html/body/main/section/section/div[2]/div/div/section/div/div[2]") == True):
        #go back 
        print("yes")
        driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]").click()
        _price += 200
        time.sleep(random.randint(2,3))
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input").click()
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input").send_keys(_price)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]").click()
        time.sleep(random.randint(1,2))  
        #increment http requests
        v = v + 5
        if(check_exists_by_xpath("/html/body/main/section/section/div[2]/div/div/section/div/div[2]") == True):  
            # increase price up to 500
            print("ni")
            _price = players[namex]
            _price += 500
            #go back 
            driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]").click()
            time.sleep(random.randint(2,3))
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input").click()
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input").send_keys(_price)
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]").click()
            time.sleep(random.randint(1,2))
            print("yada")
            #increment http requests
            v = v + 5
            if(check_exists_by_xpath("/html/body/main/section/section/div[2]/div/div/section/div/div[2]") == True):  
                #go back
                time.sleep(random.randint(2,3))
                driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]").click()
                print("waddup")
                return()
            else:
                print("ok")
                players[namex] += 500
                #go back 
                time.sleep(random.randint(2,3))
                driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]").click()
                #increment http requests
                v = v + 1
                return()
        else:
            print("waddup")
            players[namex] += 300
            #go back 
            time.sleep(random.randint(2,3))
            driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]").click()
            #increment http requests
            v = v + 1
            return()
    else:
        #go down in price....
        #go back 
        print("urup")
        time.sleep(random.randint(2,3))
        driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]").click()
        _price = players[namex]
        _price -= 200
        time.sleep(random.randint(2,3))
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input").click()
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input").send_keys(_price)
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]").click()
        time.sleep(random.randint(1,2))
        #increment http requests
        v = v + 4
        if(check_exists_by_xpath("/html/body/main/section/section/div[2]/div/div/section/div/div[2]") == True):
            driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]").click()
            time.sleep(random.randint(2,3))
            _price = players[namex]
            _price -= 500
            #go back 
            print("imu[")                   
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input").click()
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input").send_keys(_price)
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]").click()
            time.sleep(random.randint(1,2))
            #increment http requests
            v = v + 5
            if(check_exists_by_xpath("/html/body/main/section/section/div[2]/div/div/section/div/div[2]") == True):
                #increment http requests
                v = v + 1
                #go back
                is_available = False
                time.sleep(random.randint(2,3))
                driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]").click()
                return()
            else:
                players[namex] -= 300
                # go back
                time.sleep(random.randint(2,3))
                driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]").click()
                #increment http requests
                v = v + 1
                return()
        else:
            print("whosup")
            players[namex] -= 100
            # go back
            time.sleep(random.randint(2,3))
            driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]").click()
            #increment http requests
            v = v + 1
            return()
        


# trying to snipe marcus rashford
i = 0
def getcode():
    print("yup")
    windows = driver.window_handles
    time.sleep(2)
    driver.switch_to.window(windows[0])
    time.sleep(2)
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    s = driver.current_url
    time.sleep(4)
    #sign in
    driver.find_element_by_xpath("/html/body/header/div/aside/div/nav/ul/li[2]").click()
    # put in email and password
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]").send_keys("") # password for hotmail
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/input").click()
    # put in password
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/input").send_keys("") #password for hotmail
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input").click()
    #click on other tab
    time.sleep(15)                       
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[1]/div[1]/div/div[2]/div/div[1]/button[2]").click()
    #click on first email
    time.sleep(6)                     
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div[2]").click()
    time.sleep(12)                                                    
    for element in driver.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/span[2]/b"):
        codex = element.text
        return(codex)
        print(codex)
    global v
    v = v + 9    

def randomised():
    # randomly click when in transfer market
    x = random.randint(1,3)
    if(x == 1):
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[1]")
    if(x == 2):
        driver.find_element_by_xpath("/html/body/main/section/section/div[1]")
    if(x == 3):
        driver.find_element_by_xpath("/html/body/div[1]")
    global v
    v += 3
def makebid(x = ""):
    #loop through each available player when in the transfer market
    #bid on each player that is under the 20 minute mark
    time.sleep(random.randint(2,3))
    print("cannot")
    ix = 0
    pe = 1
    global v
    while(ix == 0):
        if(check_exists_by_xpath("/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[" + str(pe) +"]/div/div[2]/div[4]/span[2]")):
            time1x = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[" + str(pe) +"]/div/div[2]/div[4]/span[2]").text
            u = 0
            time1y = ""
            time1z = ""
            while(u < len(time1x)):
                if(time1x[u].isdigit()):
                    time1y += time1x[u]
                else:
                    time1z += time1x[u]
                u += 1
            time1 = int(time1y)
            print(time1z)
            # check if rashford was found,,,,
            if(driver.find_elements_by_xpath("/html/body/main/section/section/div[2]/div/div/section/div/div[2]/div/span")):
                # go back
                driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]").click()
            else:
                if(time1 < 46 and time1z == " Minutes" or time1z == " Seconds"):
                    # bid on first player 
                    time.sleep(random.randint(1,3))
                    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[" + str(pe) +"]").click()
                    # set bid value
                    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div/input").click()
                    time.sleep(1)
                    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div/input").send_keys(x)
                    #make the bid
                    time.sleep(random.randint(1,3))
                    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[1]").click()
                else:
                    ix = 1
                    # go back
                    driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]").click()
            pe += 1
        else:
            # go back
            driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]").click()
            ix = 1
            v = v + 1
        v = v + 9



def playerdets(id4 = " ", f1 = 0, n1 = "",idno = 0):  
    #increment http requests
    global v
    print(v)
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/input").click()
    time.sleep(random.randint(1,3))
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/input").send_keys(unidecode.unidecode(n1))
    time.sleep(random.randint(1,3))
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div/ul/button[1]").click()
    time.sleep(random.randint(1,3))
    xy = threading.Thread(target=check_player,args = ("0", playernames[idno]))
    xy.start()
    xy.join()
    _bidvalue = players[n1] - 500
    sellingprice[n1] = _bidvalue
    if(is_available == True):
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input").clear()
        time.sleep(random.randint(2,4))
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/input").click()
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/input").send_keys(_bidvalue)
        time.sleep(random.randint(1,3))
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]").click()
        players[n1] = f1
        makebid(_bidvalue) 
        v = v + 7
   

    



if __name__ == "__main__":
    main()

