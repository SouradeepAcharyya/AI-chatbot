import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather
def Action(data):
    user_data = data.lower()
    if "what is your name" in user_data:
       text_to_speech.text_to_speech("My name is virtual assistant....I am Souradeep's AI assistant..I was built by Souradeep")
       return "My name is virtual assistant....I am Souradeep's AI assistant..I was built by Souradeep"
    elif "hello" in user_data or "hi" in user_data or "hye" in user_data:
       text_to_speech.text_to_speech("Hello Sir!! How I can help you ?")
       return "Hello Sir!! How I can help you ?"
    elif "Good Morning" in user_data or "good morning" in user_data:
       text_to_speech.text_to_speech("Good morning sir")
       return "Good morning sir"
    elif "Good Night" in user_data or "good night" in user_data:
       text_to_speech.text_to_speech("Good night sir..sleep well")
       return "Good night sir..sleep well"   
    elif "Time now" in user_data or "What is the time" in user_data or "What is the time now" in user_data:
       current_time = datetime.datetime.now()
       Time = (str)(current_time) + " Hour :", (str)(current_time.minute) + " Minute"
       text_to_speech.text_to_speech(Time)
       return Time
    elif "shutdown" in user_data:
       text_to_speech.text_to_speech("Okay sir..Have a good day")
       return "Okay sir..Have a good day"
    elif "play music" in user_data:
       webbrowser.open("https://gaana.com/")
       text_to_speech.text_to_speech("gaana.com is now ready for you")
       return "gaana.com is now ready for you"
    elif "open google" in user_data:
       webbrowser.open("https://google.com/")
       text_to_speech.text_to_speech("google.com is opened for you")
       return "google.com is opened for you"
    elif "open youtube" in user_data:
       webbrowser.open("https://youtube.com/")
       text_to_speech.text_to_speech("youtube.com is opened for you")
       return "youtube.com is opened for you"
    elif "weather" in user_data:
       ans = weather.weather()
       text_to_speech.text_to_speech(ans)
       return ans   
    else:
       text_to_speech.text_to_speech("I am not able to understand")
       return "I am not able to understand"
       




