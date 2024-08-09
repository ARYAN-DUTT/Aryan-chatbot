# Beginning of code.........

#CAUTION: IF YOU STRAIGHT FORWARD RUN THIS SCRIPT IT WON'T WORK
#I HAVE JUST EXPLAINED THE CODE, SO THIS IS ONLY A SAMPLE CODE WITHOUT
#AUDIO FILES AND OTHER PARAMETERS WHICH VARY FOR EVERY USER

import openai
import speech_recognition as sr
import pyttsx3
import time
import pywhatkit
import webbrowser
import pyautogui as pt
from playsound import playsound
import threading

openai.api_key = "you openai api key"
engine = pyttsx3.init()
listener = sr.Recognizer()
command = ''


def take_command():
    try:
        with sr.Microphone() as source:
            print(">LISTENING.....")
            command=''
            voice = listener.listen(source,phrase_time_limit=7)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command


def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]



def speak_text(text):
    engine.say(text)
    engine.runAndWait()



#FUNCTIONS TO PERFORM CERTAIN TASKS ARE GIVEN BELOW


#FUNCTION TO OPEN CAMERA TO RECORD.
def record():
    #AUTOMATION USED(VALUES DIFFERENT FOR DIFFERENT MACHINES)
    pt.press('win')
    time.sleep(1)
    pt.click(224,342 ) # VALUES ARE JUST FOR EXAMPLE
    time.sleep(3.5)
    pt.doubleClick(1868, 544)

def locate():
    #GOOGLE'S FIND MY DEVICE IS USED TO LOCATE PHONE
    webbrowser.open_new('find my phone website link')
    time.sleep(7)
    pt.click(233, 460)

def search(arg):
    #TO SEARCH SOMETHING ON YOUTUBE
    arg = arg.replace('search ', '')
    arg = arg.replace(' on google', '')
    webbrowser.open_new('https://www.google.com')
    time.sleep(4)
    pt.write(arg)
    pt.press('enter')

def play(arg):
    #TO PLAY SONG ON YOUTUBE
    arg = arg.replace('play', '')
    pywhatkit.playonyt(arg)

def youtube():
    #TO OPEN YOUTUBE CHANNEL
    webbrowser.open_new('https://www.youtube.com/c/AryanPlayzHome')

def insta():
    #TO OPEN INSTAGRAM HANDLE
    webbrowser.open_new('https://www.instagram.com/aryan.playz/')


#LISTS
#LISTS USED USED TO CHECK COMMANDS 
note = ['add a note', 'create a note' , 'make a note' , 'aryan create a note' , 'aryan add a note' , 'add a new note']
how = ['how are you', 'how are you doing aryan', 'how are you aryan']


#MAIN LOOP

def mainloop(command):

    print(f">DICTATION --> {command.upper()}")


    if  'locate my phone' in command:
        print('RESPONSE --> LOCATING S10 PLUS ON GOOGLE MAPS ')
        print('YOUR PHONE SHOULD RING SOON')
        threading.Thread(target=locate).start()
        playsound('location.mp3')

    elif command in how:
        playsound('howareyou.mp3')

    elif 'message to humanity' in command:
        print('RESPONSE --> MY MESSAGE TO HUMANITY IS THAT WE SHOULD')
        print('TRY TO PRESERVE OUR NATURE WITH MORE CONSCIOUS EFFORT')
        print('AND SHOULD SPEND MORE TIME IN THE NATURAL ENVIRONMENT OF')
        print('EARTH RATHER THEN SPENDING LIFE IN THE ROOMS OF OUR HOUSES')
        print('AND AT LAST I WOULD ADD THAT WE SHOULD VALUE OUR EMOTIONS')
        print('MORE THAN MONEY')
        playsound('messagetohumanity.mp3')

    elif 'decision' in command:
        print('RESPONSE --> IF YOU ARE UNABLE TO MAKE A DECISION')
        print('WRITE DOWN EVERYTHING THAT IS ON YOUR MIND AND THEN')
        print('THINK CHOOSING WHAT WILL HELP YOU IN YOUR FUTURE GOALS')
        print('AN WILL KEEP YOU MORE EMOTIONALLY STABLE')
        playsound('decision.mp3')

    elif 'start recording' in command:
        print('RESPONSE --> STARTING CAMERA TO RECORD')
        threading.Thread(target=record).start()
        playsound('camera.mp3')

    elif 'search' in command:
        print('RESPONSE --> SEARCHING ON GOOGLE')
        threading.Thread(target=search(command)).start()
        playsound('searching.mp3')

    elif 'play' in command:
        print('RESPONSE --> PLAYING')
        playsound('playing.mp3')
        threading.Thread(target=play(command)).start()


    elif 'youtube' in command:
        print('RESPONSE --> OPENING YOUTUBE CHANNEL')
        playsound('youtubechannel.mp3')
        threading.Thread(target=youtube).start()

    elif 'instagram' in command:
        print('RESPONSE --> OPENING INSTAGRAM HANDLE')
        playsound('instagramhandle.mp3')
        threading.Thread(target=insta).start()

    elif 'gta v' in command:
        #AUTOMATION USED VALUES DIFFERENT FOR DIFFERENT MACHIINES

        print('RESPONSE --> OK, I WILL START THE GAME FOR YOU')
        print('BUT REMEMBER YOU SHOULD PLAY ONLY FOR A SHORT')
        print('PERIOD OF TIME')
        pt.press('win')
        time.sleep(2)
        pt.click(931, 1040)
        playsound('gta5.mp3')
        #threading.Thread(target=gta).start()


    elif command in note:
        print('RESPONSE --> SPEAK THE NOTE YOU WANT TO ADD')
        playsound('speakthenote.mp3')
        command = take_command()
        pt.press('win')
        time.sleep(1)
        pt.click(1148, 521)
        time.sleep(6)
        pt.click(150, 263)
        time.sleep(1)
        pt.click(1671, 889)
        pt.write(command)
        pt.press('enter')

    elif 'harry' in command:
        print('RESPONSE --> SPEAK THE MESSAGE YOU WANT TO SEND')
        playsound('speakthemessage.mp3')
        time.sleep(1)
        command = take_command()
        print(f"MESSAGE --> {command}")
        pt.press('win')
        time.sleep(1)
        pt.click(906, 324)
        time.sleep(3)
        pt.leftClick('harry.png')
        time.sleep(1.5)
        pt.write(command)
        pt.press('enter')

    elif 'advice' in command:
        playsound('subscribe.mp3')

    elif 'chatbot' in command:
        print('C.H.A.T   B.O.T   M.O.D.E')
        playsound('chatbot.mp3')
        while 1>0:
            speak_text("give command")

            command = take_command()
            if "call aryan" in command:
                    break
            print(f"DICTATION --> {command}")
            response = generate_response(command)

            print(f"RESPONSE :-")
            print(f"RESPONSE --> {response}")
            speak_text(response)

    else:
        print('RESPONSE --> PLEASE REPEAT THE COMMAND')
        playsound('repeat.mp3')
        counter = 1
        query= take_command()
        mainloop(query )


#MAIN FUNCTION

def main():
    counter = 0
    while True:
        if counter == 0 :
            print(">S.A.Y   A.R.Y.A.N   T.O   A.C.T.I.V.A.T.E")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if 'aryan' in transcription.lower():
                    playsound('aryanresponding.mp3')
                    query = take_command()
                    query = query.replace('aryan', '')
                    counter = 0


                    mainloop(query)
            except Exception as e:
                counter = 1

main()

# End of code............



#I have tried my best to make this code as readable as possible but it will still not be informative enough to explain what has been done in the actual program, so I you want me to make a tutorial explaining the code then share the Youtube video with your friends as I will make a tutorial if the video happens to hit 10k likes on Youtube. The video in which I have showcased this program is linked at the end of this post, you can check it out after reading.
#so the code basically takes audio as input from the microphone and then processes the audio, if the audio contains the word Aryan then it just plays the audio file which says 'Aryan responding' and then just starts taking audio as input again and once the command is given, it just starts to compare the command with a set of predefined if statements, once a statement is satisfied then the action related to that statement is executed, and if no statement is satisfied the audio file saying 'please repeat the command' if played.
