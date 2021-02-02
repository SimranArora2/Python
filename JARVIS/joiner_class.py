# Schedule Library imported 
import schedule 
import time 
import datetime
from webbrowser import open
import pyautogui as aa
from time import sleep

def class_opening(entering):
    sleep(7)
    aa.press('tab')
    sleep(1)
    aa.typewrite('20BCS3400')
    sleep(1)
    aa.press('tab')
    sleep(1)
    aa.typewrite('2@Sem2')
    sleep(1)
    aa.press('tab')
    sleep(1)
    aa.press('enter')
    sleep(10)
    aa.press('tab')
    sleep(1)
    aa.press('enter')
    sleep(1)
    aa.press('tab')
    sleep(1)
    aa.press('tab')
    sleep(1)
    aa.press('enter')
    sleep(1)
    aa.press('down')
    sleep(1)
    aa.press('enter')
    sleep(30)
    ######################################################################################
    aa.press('tab')
    sleep(1)
    aa.press('tab')
    sleep(1)
    aa.press('enter')
    sleep(1)
    aa.press('tab')
    sleep(1)
    #aa.typewrite('Good Morning')
    if datetime.datetime.now().hour<12:
        aa.typewrite('Good Morning {}'.format(entering))
    else:
        aa.typewrite('Good afternoon {}'.format(entering))
    sleep(1)
    aa.press('enter')
    sleep(3350)
    aa.hotkey('altleft','f4')

# Functions setup 
def maths():
    open('https://cuchd.blackboard.com/ultra/courses/_8976_1/outline')
    sleep(3)
    aa.hotkey('altleft','f4')
    sleep(2)
    open('https://cuchd.blackboard.com/ultra/courses/_8976_1/outline')
    class_opening('ma\'am')
    
def prog():
    open('https://cuchd.blackboard.com/ultra/courses/_8055_1/outline')
    sleep(3)
    aa.hotkey('altleft','f4')
    sleep(2)
    open('https://cuchd.blackboard.com/ultra/courses/_8055_1/outline')
    class_opening('sir')

def prog_lab():
    open('https://cuchd.blackboard.com/ultra/courses/_7970_1/outline')
    sleep(3)
    aa.hotkey('altleft','f4')
    sleep(2)
    open('https://cuchd.blackboard.com/ultra/courses/_7970_1/outline')
    class_opening('sir')

def bio():
    open('https://cuchd.blackboard.com/ultra/courses/_9506_1/outline')
    sleep(3)
    aa.hotkey('altleft','f4')
    sleep(2)
    open('https://cuchd.blackboard.com/ultra/courses/_9506_1/outline')
    class_opening('ma\'am')

def communication_skill():
    open('https://cuchd.blackboard.com/ultra/courses/_9530_1/outline')
    sleep(3)
    aa.hotkey('altleft','f4')
    sleep(2)
    open('https://cuchd.blackboard.com/ultra/courses/_9530_1/outline')
    class_opening('ma\'am')

def communication_skill_lab():
    open('https://cuchd.blackboard.com/ultra/courses/_9526_1/outline')
    sleep(3)
    aa.hotkey('altleft','f4')
    sleep(2)
    open('https://cuchd.blackboard.com/ultra/courses/_9526_1/outline')
    class_opening('ma\'am')

def CAD():
    open('https://cuchd.blackboard.com/ultra/courses/_8628_1/outline')
    sleep(3)
    aa.hotkey('altleft','f4')
    sleep(2)
    open('https://cuchd.blackboard.com/ultra/courses/_8628_1/outline')
    class_opening('sir')

def DE():
    open('https://cuchd.blackboard.com/ultra/courses/_9496_1/outline')
    sleep(3)
    aa.hotkey('altleft','f4')
    sleep(2)
    open('https://cuchd.blackboard.com/ultra/courses/_9496_1/outline')
    class_opening('sir')

def DE_lab():
    open('https://cuchd.blackboard.com/ultra/courses/_8121_1/outline')
    sleep(3)
    aa.hotkey('altleft','f4')
    sleep(2)
    open('https://cuchd.blackboard.com/ultra/courses/_8121_1/outline')
    class_opening('sir')

def AI_lab():
    open('https://cuchd.blackboard.com/ultra/courses/_8155_1/outline')
    sleep(3)
    aa.hotkey('altleft','f4')
    sleep(2)
    open('https://cuchd.blackboard.com/ultra/courses/_8155_1/outline')
    class_opening('sir')

def Mentoring():
    open('https://cuchd.blackboard.com/ultra/courses/_9544_1/outline')
    sleep(3)
    aa.hotkey('altleft','f4')
    sleep(2)
    open('https://cuchd.blackboard.com/ultra/courses/_9544_1/outline')
    class_opening('sir')
    

# Every tuesday at 18:00 sudo_placement() is called 
schedule.every().monday.at("09:50").do(maths) 
schedule.every().monday.at("10:50").do(prog)
schedule.every().monday.at("11:50").do(prog_lab)
schedule.every().monday.at("13:35").do(AI_lab)
schedule.every().monday.at("14:35").do(AI_lab)

schedule.every().tuesday.at("09:50").do(DE) 
schedule.every().tuesday.at("10:57").do(bio)
schedule.every().tuesday.at("11:50").do(maths)
schedule.every().tuesday.at("13:35").do(prog)
schedule.every().tuesday.at("14:35").do(prog_lab)

schedule.every().wednesday.at("09:50").do(communication_skill_lab) 
schedule.every().wednesday.at("10:50").do(communication_skill_lab)
schedule.every().wednesday.at("11:50").do(maths)
schedule.every().wednesday.at("13:35").do(communication_skill)
schedule.every().wednesday.at("14:35").do(CAD)

schedule.every().thursday.at("09:50").do(CAD) 
schedule.every().thursday.at("10:50").do(CAD)
schedule.every().thursday.at("11:50").do(DE)
schedule.every().thursday.at("13:35").do(prog_lab)
schedule.every().thursday.at("14:35").do(prog_lab)

schedule.every().friday.at("09:50").do(communication_skill) 
schedule.every().friday.at("10:50").do(bio)
schedule.every().friday.at("11:50").do(Mentoring)
schedule.every().friday.at("13:35").do(DE)

schedule.every().saturday.at("09:50").do(maths) 
schedule.every().saturday.at("10:50").do(DE_lab)
schedule.every().saturday.at("11:50").do(DE_lab)
schedule.every().saturday.at("13:35").do(bio)

# Loop so that the scheduling task 
# keeps on running all time. 
while True: 
  
    # Checks whether a scheduled task  
    # is pending to run or not 
    schedule.run_pending() 
    time.sleep(1)