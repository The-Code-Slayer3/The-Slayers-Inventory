import msvcrt,wikipedia, pywhatkit as pykt, speech_recognition as sr,pkg_resources,pyttsx3
from datetime import datetime
from subprocess import call
voice_processor = pyttsx3.init('sapi5')

ch_voice=int(input("for Male Voice Enter 1, for Female voice enter 2\n"))
match ch_voice:
    case 1:
        # voice[0].id ie male
        print("You Chose Nolan...")
        voice_processor.setProperty('voice', voice_processor.getProperty('voices')[0].id)
    case 2:
        #voice[1].id ie. female
        print("You Chose Lacey....")
        voice_processor.setProperty('voice',voice_processor.getProperty('voices')[1].id)

voice_processor.setProperty('volume',1.0)
voice_processor.setProperty('rate',155)

def speak(text):
    voice_processor.say(text)
    voice_processor.runAndWait()

def greet():
    hour = datetime.now().hour
    if 6<hour<12:
        match ch_voice:
            case 1:
                speak("Good Morning, I'm Nolan")
            case 2:
                speak("Good Morning, I'm lacey")
    elif 12<hour<18:
        match ch_voice:
            case 1:
                speak("Good Afternoon, I'm Nolan")
            case 2:
                speak("Good Afternoon, I'm lacey")
    else:
        match ch_voice:
            case 1:
                 speak("Good Evening I'm Nolan")
            case 2:
                 speak("Good Evening I'm lacey")

def Userinput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1.125 # rate of speaking of the user, sr= amt of words/time taken
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source)
    try:
        print('recognising....')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None"
    return query
if __name__ == '__main__':
    greet()
    while True:
        query= Userinput().lower()
        if "exit" in query:
            speak("Thank You")
            break

        if "change voice" in query:
            speak("Okay, choose your voice....., enter 1 for male 2 for female")
            ch_voice=int(input())
            match ch_voice:
                case 1:
                    voice_processor.setProperty('voice', voice_processor.getProperty('voices')[0].id)
                    speak("Thank You, Lacey")
                case 2:
                    voice_processor.setProperty('voice', voice_processor.getProperty('voices')[1].id)
                    speak("Thank You, Nolan")
            speak("Voice Change Complete..... let's proceed....")

        if "update" in query:
            speak("Ok. Checking for updates.....")
            call("pip install --upgrade --no-cache-dir " + ' '.join([dist.project_name for dist in pkg_resources.working_set]), shell=True)
            msvcrt.getch()

        if "wait" in query:
            speak("Ok, Press Enter When You want to call me")
            msvcrt.getch()

        if "wikipedia" in query:
               query.replace('wikipedia',"")
               results=wikipedia.summary(query, sentences=4)
               print(results)
               speak(results)
               msvcrt.getch()
        
        if "youtube" in query:
            speak("Okay, I'll Playing it now")
            pykt.playonyt(query)
            speak("I'll be waiting in Background, press enter when finished to proceed..")
            print("Press Enter to continue..")
            msvcrt.getch()

        if "google" in query:
            query.replace("google", "")
            pykt.search(query)
            speak("I'll be waiting in Background, press enter when finished to procced..")
            print("Press Enter to Continue....")
            msvcrt.getch()
