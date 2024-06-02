import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os


engine=pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#speak("hello sirrr")
#speak("what's the time now" )
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    #speak("Today's time is")
    speak(Time)
    #speak("this is the present time sirr")
    #speak("what's the date")
def date():
    Year=int(datetime.datetime.now().year)
    Month=int(datetime.datetime.now().month)
    Day=int(datetime.datetime.now().day)
    #speak("today's date is")
    speak(Day)
    speak(Month)
    speak(Year)
def wishme():
    speak("welcome back sir")
    time()
    date()
   
    hour=datetime.datetime.now().hour
    if (hour>0 and hour<=12):
        speak("it's morning sirr")
    elif(hour>=12 and hour<=18):
        speak("its evening sirr")
    elif(hour>18 and hour<=23):
        speak("its night sirr")
    speak("iam jarvis iam under your service what can i do for you sirr ")    
wishme()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognation")
        query=r.recognize_google(audio,language='en-in')
        print(query)
    except Exception as ex:
        print(ex)
        speak("cannot understand please repete")
        return"none"
    return query
takeCommand()
def sendEmail(to,content):#for email sending process
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('shomeshwarren458@gmail.com','domnicktoorato12345')
    server.sendmail('shomeshwarren458@gmail.com',to,content)
    server.close()
if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("searching...")
            query=query.replace("wikipedia","")
            try:
                result = wikipedia.summary(query, sentences=10)
                speak("According to Wikipedia")
                print(result)
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for your query, please be more specific")
            except wikipedia.exceptions.PageError as e:
                speak("I couldn't find any results for your query, please try again")
            except Exception as e:
                speak("An error occurred while searching Wikipedia")    
        elif 'mail to' in query:
            try:
                speak("what should i say ?")
                content=takeCommand()
                to='shomeshhack@gmail.com'
                sendEmail(to,content)
                speak("email has been send!")
            except Exception as e:
                print(e)
                speak("unnable to understand please repete it sirr")
        elif 'search in chrome' in query:
            speak("what do you like to search sirr ?")
            chromepath='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search=takeCommand().lower()
            wb.get(chromepath).open_new_tab(f"https://www.google.com/search?q={search}")
        elif 'open youtube' in query:
            speak("opening you tube")
            chromepath='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            wb.get(chromepath).open_new_tab("https://www.youtube.com")
       # if 'close youtube' in query:
            #speak("closing you tube")
            #quit()
        elif 'play song'in query:
            song_directory='D:\movies\music'
            songs=os.listdir(song_directory)
            os.startfile(os.path.join(song_directory,songs[0]))
        elif 'logout' in query:
            os.system("shutdown -1")
        elif 'shutdown'in query:
            os.system("shutdown /s /t 1")
        elif 'restart'in query:
            os.system("shutdown /r /t 1")
        elif 'offline' in query:
            speak("going offline ,goodbye sirr.")
            break
#This is a iron man project