from os import path
import speech_recognition as sr
sr.__version__
'3.8.1'


r = sr.Recognizer()

# recognize_bing()
# recognize_google()
# recognize_houndify()
# recognize_ibm()
# recognize_spinx()
# recognize_wit()
# r.recognize_google()

#Wav, Aiff, Aiff-c, Flac (native)

# stanley = sr.AudioFile(
#     "stanley_media_radio_radio_ad_00_test_f_1b62b79b824ea004.wav")
# with stanley as source:
#     audio = r.record(source)
# type(audio)
# r.recognize_google(audio)

AUDIO_FILE = path.join(path.dirname(path.realpath(
    __file__)), "stanley_media_radio_radio_ad_00_test_f_1b62b79b824ea004.wav")

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks the audio says: " +
          r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(
        "Could not request results from Google Speech Recognition service; {0}".format(e))

print("Now you'll get another Text by another provider:")


HOUNDIFY_CLIENT_ID = "7mzn_KWsh_UqaB0vLHkUPg=="
HOUNDIFY_CLIENT_KEY = "XUSr29dzDs5CB1ZMI0-HWXwDs4XQALTO1_3JSacbkRgG5snGbm71-jQblqYTS3VJol8RLaSq7h3teDoVwIFBYw=="
try:
    print("Houndify thinks the audio says " + r.recognize_houndify(audio,
          client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
except sr.UnknownValueError:
    print("Houndify could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Houndify service; {0}".format(e))
