def test_speed():
    from pyautogui import press,typewrite
    from time import sleep
    press('win')
    sleep(2)
    typewrite('E:\speedtestoakla\speedtest.exe')
    sleep(2)
    press('enter')

def sendemail():
    #>>>>>>>>>>>>>>>>>>> GIVE AN UP VOTE IF YOU LIKED IT <<<<<<<<<<<<<<<<<<<<<

    #Easiest and Readable way to Email
    #through Python SMTPLIB library
    #This works with >>> Gmail.com <<<
    import smtplib 
    from email.message import EmailMessage

    EmailAdd = "jarvisa357@gmail.com" #senders Gmail id over here
    Pass = "anything@ican" #senders Gmail's Password over here 

    msg = EmailMessage()
    msg['Subject'] = 'hello there' # Subject of Email
    msg['From'] = EmailAdd
    msg['To'] = 'simranarora0202@gmail.com','vikramofficial2006@gmail.com' # Reciver of the Mail
    msg.set_content('hello there coding is great untill you find bugs') # Email body or Content

    #### >> Code from here will send the message << ####
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp: #Added Gmails SMTP Server
        smtp.login(EmailAdd,Pass) #This command Login SMTP Library using your GMAIL
        smtp.send_message(msg) #This Sends the message

def send_email():
    from mailer import Mailer
    print('imported')
    mail = Mailer(usr='', pwd='')
    print('id password setup')
    mail.send(receiver='simranarora0202@gmail.com', subject='TEST', message='From Python!')
    print('sent')

sendemail()
