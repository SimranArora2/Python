import pyautogui as pg
from pyttsx3 import speak
from time import sleep
def remove(string):
    return "".join(string.split())

def get_command(to_be_removed,text):
    text=str(text)  
    return text.replace(to_be_removed,'')

# def locationerrorfixer(address):
#     address=str(address)
#     return address.replace('\\','\\\\')

def send_email():
    from webbrowser import open
    import pyautogui as aa
    from time import sleep
    speak('To whom you want to send the Email')
    receiver=recognize_said_words()
    speak('speak the subject')
    subject=recognize_said_words()
    speak('speak the content')
    content=recognize_said_words()
    open("https://mail.google.com/mail/u/0/#inbox")
    sleep(5)
    sleep(1)
    aa.press('d')
    sleep(4)
    aa.typewrite(receiver)
    sleep(2)
    aa.press('tab')
    sleep(2)
    aa.press('tab')
    sleep(2)
    aa.typewrite(subject)
    sleep(2)
    aa.press('tab')
    sleep(1)
    aa.typewrite(content)
    sleep(1)
    aa.hotkey('ctrlleft','enter')
    speak('email sent succesfully ')
        

def recognize_said_words():
    import speech_recognition as sr     #import module named as speech_recognition with name sr
    r = sr.Recognizer()    #recognize the source used for speech recognition purpose
    mic = sr.Microphone(device_index=1)     #indexing micophone
    with mic as source:
        r.adjust_for_ambient_noise(source,duration=1)   #adjust to remove noise
        speak("Start saying something")
        print("Start saying something")
        audio=r.listen(source,timeout=40)    # starts listening
    try:
        speak("you said"+r.recognize_google(audio))   #print the text spoken
        # print("you said:"+r.recognize_google(audio))
        if '@' in r.recognize_google(audio):
            text = remove(r.recognize_google(audio))
            print("you said:"+text)
            return text
        else:
            print("you said:"+r.recognize_google(audio))
            return r.recognize_google(audio)
    except:     #if try fails then this part runs
        speak("sry, didn't get what you said, please repeat")
        print("sry, didn't get what you said, please repeat")
        return recognize_said_words()   #print sry if didn't get whatyytt one speaks


def run_this():
    #isEntryAllowed=False
    input_command=recognize_said_words()
    if 'hey jarvis' or 'hi jarvis' or 'hello jarvis' or 'jarvis' == input_command:
        #recognize using username and password
        speak('are you an old user')
        print("are you an old user")
        old_user_or_not=recognize_said_words()
        if 'yes' in old_user_or_not:
            speak('speak your username')
            print("speak your username")
            username=recognize_said_words()
            speak('speak your password')
            print("speak your password")
            password=recognize_said_words()
            try:
                filename = open(r'D:\\SIMU\\AI\\JARVIS\\{}password.txt'.format(username),"r")
                str = filename.readline()
                if password in str:
                    isEntryAllowed = True
                    commands(isEntryAllowed=True)
                else:
                    speak('entry not allowed')
                    isEntryAllowed = False
                    commands(isEntryAllowed=False)
                    run_this()
                filename.close()
            except Exception as e:
                print(e)
                run_this()
        elif 'no' in old_user_or_not:
            speak("to continue you need to signup day yes if you want to continue else no")
            print("to continue you need to signup day yes if you want to continue else no")
            want_to_signup_or_not=recognize_said_words()
            if 'yes' in want_to_signup_or_not:
                speak("enter new username")
                print("enter new username")
                new_user_name = recognize_said_words()
                speak('enter new password')
                print("enter new password")
                new_password = recognize_said_words()
                filename = open(r'D:\\SIMU\\AI\\JARVIS\\{}.txt'.format(new_user_name),"a+")
                str1 = filename.readline()
                print(filename.write(new_user_name+"\n"),end='')
                filename.close()
                filename = open(r'D:\\SIMU\\AI\\JARVIS\\{}password.txt'.format(new_user_name),"a+")
                str2 = filename.readline()
                print(filename.write(new_password+"\n"),end='')
                filename.close()
                speak('now you have to sign in to use our service')
                print("now you have to sign in to use our service")
                run_this()
            elif 'no' in want_to_signup_or_not:
                speak('sorry madam then you will be unable to continue')
                print("sorry madam then you will be unable to continue")
            else:
                speak('enter valid input')
                print("enter valid input")
                run_this()
        else:
            speak('enter valid input')
            print("enter valid input")
            run_this()
    else:
        speak('enter valid input')
        print("enter valid input")
        run_this()

def commands(isEntryAllowed=False):
    speak('Welcome madam')
    print("Welcome madam")
    hourA = 22
    minA = 33
    import datetime
    import datefinder
    import winsound
    while isEntryAllowed==True:
        if hourA == datetime.datetime.now().hour:
            if minA == datetime.datetime.now().minute:
                # print("your alarm rang")
                # winsound.PlaySound('audio file')
                print("your alarm rang")
                #from playsound import playsound
                #playsound('audio.mp3')
                isalarmringing=True
                while isalarmringing==True:
                    winsound.PlaySound("C:\\Users\\91999\\AppData\\Local\\Programs\\Python\\Python37\\1st Semester\\Jarvis\\08 - Dhoom Machale Dhoom - Arabic.mp3",winsound.SND_LOOP)
                    import cv2
                    # key = waitKey(1)
                    key = cv2.waitKey(1)
                    if hourA != datetime.datetime.now().hour:
                        if minA != datetime.datetime.now().minute:
                            break
                    if key==81 or key==113:
                        break
                    elif key==83 or key==115:
                        if minA<55:
                            minA=minA+5
                        else:
                            new_min=60-minA
                            if hourA<24:
                                hourA=hourA+1
                                minA=minA+new_min
                            else:
                                hourA=0
                                minA=minA+new_min
        print("what you want me to do for you madam")
        speak('what you want me to do for you madam')
        user_input = recognize_said_words()
        if 'Wi-Fi' in user_input:
            print("searching for wifi")
            speak('searching for wifi')
            from os import system
            system('netsh wlan show profiles')
        elif 'connect to nearby network' in user_input:
            print("connecting to nearby network")
            speak('connecting to nearby network')
            from os import system
            system('netsh wlan connect name="Galaxy M51F2F0 Simran Arora"')
            speak('Connection request was completed successfully')
        elif 'classes' in user_input:
            speak('Activating Automatic Class Joiner')
            from webbrowser import open
            import pyautogui as aa
            from time import sleep
            open('https://cuchd.blackboard.com/ultra/course')
            sleep(5)
            aa.hotkey('altleft','f4')
            from os import system   
            system('joiner_class.py') 
        elif 'snake' in user_input:
            print("going to play snake game")
            speak('going to play snake game')
            from os import system
            system('python snake.py')
        elif 'play' and 'on YouTube' in user_input:
            print("playing")
            speak('playing')
            from pywhatkit import playonyt
            playonyt(user_input)
        elif 'BB' in user_input:
            from webbrowser import open
            import pyautogui as aa
            from time import sleep
            open('https://cuchd.blackboard.com/?new_loc=%2Fultra%2Fcourse')
            sleep(2)
            aa.press('tab')
            aa.press('tab')
            aa.press('tab')
            aa.press('enter')
        elif 'open' in user_input:
            from time import sleep
            from pyautogui import press,typewrite
            user_input=str(user_input)
            user=user_input[5:]
            #new_user_input=str(get_command('open ',user_input))
            press('win')
            sleep(2)
            typewrite(user)
            sleep(2)
            press('enter')
            #→ Opening any installed application
        elif 'message' in user_input:
            from pywhatkit import sendwhatmsg
            print("speak mobile no to which you want to send")
            speak('speak mobile no to which you want to send')
            phone_number=str(recognize_said_words())
            #phone_number=str(phone_number)
            phone_number='+91'+phone_number
            "".join(phone_number.split())
            print(phone_number)
            print("speak the message")
            speak('speak the message')
            message=recognize_said_words()
            print("when to send note time must be of 2 minutes later")
            speak('when to send note time must be of 2 minutes later')
            hours=recognize_said_words()
            print("minutes")
            speak('minutes')
            minutes=recognize_said_words()
            sendwhatmsg(phone_number,message,int(hours),int(minutes))
            #Send messages on whats app
        elif 'covid-19' in user_input:
            from covid_19_tracker import tracker
            tracker()
            #covid19 tracker and represent on gui=Vikram
        elif 'search ' in user_input:
            from pywhatkit import search
            #new_user_input=get_command('search on google ',user_input)
            user_input_new = user_input[7:]
            search(user_input_new)
            #→  Searching on google
        elif 'chess' in user_input:
            #Chess = Simran
            print("opening chess lets play")
            speak('opening chess lets play')
            from os import system
            system('python gui.py')
        elif 'detect language' in user_input:
            #detect language
            print("speak the sentence")
            speak('speak the sentence')
            to_be_detected=recognize_said_words()
            from langdetect import detect
            print(detect(to_be_detected))
            speak(detect(to_be_detected))
        elif 'translate' in user_input:
            #Translater
            print("speak the sentence which you want to translate")
            speak('speak the sentence which you want to translate')
            to_be_detected=recognize_said_words()
            to_be_translated = str(to_be_detected)
            from langdetect import detect
            #pip or conda install googletrans
            from translate import Translator
            # print("Language of the sentence in which sentence you spoken")
            # speak("Language of the sentence in which sentence you spoken")
            first_lang = detect(to_be_detected)

            print("In which language you want to translate your sentence")
            speak("In which language you want to translate your sentence")
            second_lang = str(recognize_said_words()) 

            translator= Translator(from_lang = first_lang,to_lang = second_lang)           
            #you can specify the translate languege
            result = translator.translate((to_be_translated))
            print(result)
            speak(result)
        elif 'internet speed' in user_input:
            from pyautogui import press,typewrite
            import pyautogui as aa
            from time import sleep
            from os import startfile 
            startfile('speedtest.exe')
            sleep(30)
            # aa.hotkey('altleft','F4')
        elif 'alarm' in user_input:
            speak("speak hours")
            print("speak hours")
            hourA = int(recognize_said_words())
            speak("speak minutes")
            print("sprak minutes")
            minA = int(str(recognize_said_words))
            # get_command('alarm',user_input)
            # dTimeA = datefinder.find_dates(user_input)
            # mat=()
            # for mat in dTimeA:
            #     print(mat)
            # stringA = str(mat)
            # timeA = stringA[11:]
            # hourA = timeA[:-6]
            # hourA = int(hourA)
            # minA = timeA[3:-3]
            # minA = int(minA)
        elif 'image' in user_input:
            import cv2
            camera = cv2.VideoCapture(0)
            return_value, image = camera.read()
            cv2.imwrite('image1.png', image)
            del(camera)
        elif 'Ludo' in user_input:
            from os import system
            system('python ludo.py')
        elif 'play snake game' in user_input:
            from os import system
            system('python snake.py')
        elif 'shutdown' in user_input:
            from pywhatkit import shutdown
            speak('going to shut  down your system in 30 seconds')
            shutdown(time=30)
        elif 'Tic Tac Toe' in user_input:
            from os import system
            system('python tic_tac_toe.py')
        elif 'email' in user_input:
            from webbrowser import open
            import pyautogui as aa
            from time import sleep
            speak('To whom you want to send the Email')
            receiver=recognize_said_words()
            # receiver.replace(" ","")
            speak('speak the subject')
            subject=recognize_said_words()
            speak('speak the content')
            content=recognize_said_words()
            open("https://mail.google.com/mail/u/0/#inbox")
            sleep(14)
            aa.press('d')
            sleep(7)
            #aa.press('tab')
            #sleep(7)
            aa.typewrite(receiver)
            sleep(2)
            aa.press('tab')
            sleep(2)
            aa.press('tab')
            sleep(2)
            aa.typewrite(subject)
            sleep(2)
            aa.press('tab')
            sleep(1)
            aa.typewrite(content)
            sleep(1)
            aa.hotkey('ctrlleft','enter')
            speak('email sent succesfully ')
        elif 'movie' in user_input:
            from webbrowser import open
            import pyautogui as aa
            from time import sleep
            speak('madam you having Subscriptions of Netflix, Amazon prime and Hotstar on which platform you want to watch movie')
            print('madam you having Subscriptions of Netflix, Amazon prime and Hotstar on which platform you want to watch movie')
            user_input_new = recognize_said_words()
            if 'Prime' in user_input_new:
                speak('opening primevideo')
                open('https://www.primevideo.com/?ref_=dvm_pds_amz_in_as_s_g_146|m_lgAX6a65c_c386561644245')
                break
            elif 'Netflix' in user_input_new:
                speak('opening netflix')
                open('https://www.netflix.com/browse')
                break
            elif 'Hotstar' in user_input_new:
                speak('opening hotstar')
                open('https://www.hotstar.com/in')
                break
        elif 'calculate' in user_input:
            from os import system
            system('calculator.py')
        elif 'zip' in user_input:
            from os import system
            system('python zip_file.py')
        elif 'face' in user_input:
            import cv2
            import pyautogui as aa
            from random import randrange
            from time import sleep
            # Load some pre-trained data on face frontals from opencv (hear cascade algorithm)
            trained_face_data=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            camera = cv2.VideoCapture(0)
            while True:
                succesful_frame_read,frame = camera.read()
                grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
                for (x,y,w,h) in face_coordinates:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),10)
                cv2.imshow('JARVIS: EYES',frame)
                key = cv2.waitKey(1)
                if key==81 or key==113:
                    del(camera)
                    break
        elif 'sleep' in user_input:
            from time import sleep
            speak('For how much time you want me to sleep in seconds')
            print('For how much time you want me to sleep in sec.')
            time=recognize_said_words()
            speak('Going to sleep')
            T=int(time[:-7])
            sleep(T)
        
        elif 'stop' in user_input:
            return 0

#run_this()

commands(isEntryAllowed=True)