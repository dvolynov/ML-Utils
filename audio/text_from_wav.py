import speech_recognition as sr


def text_from_wav(path, language="ru-RU"):
    sample = sr.WavFile(path)
    r = sr.Recognizer()

    with sample as audio:
        content = r.record(audio)
        r.adjust_for_ambient_noise(audio)

    return r.recognize_google(content, language=language)