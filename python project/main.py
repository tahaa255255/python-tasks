import speech_recognition as sr
from gtts import gTTS
from  playsound import playsound
import python_weather
import asyncio


async def getweather():
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.METRIC) as client:
    # fetch a weather forecast from a city
    weather = await client.get('cairo')
    return weather.temperature

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    talk=r.recognize_google(audio,language="ar")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
if talk == "ما هي درجة الحراره الان" or "ما هي درجة الحراره":
    tts = gTTS("درجة الحراره الان هي "+str(asyncio.run(getweather())), lang='ar')
    tts.save('speak.mp3')
    playsound("C:/Users/Tahaa Ahmed/python dev/python project/speak.mp3")