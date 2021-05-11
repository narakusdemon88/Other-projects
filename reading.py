import urllib
import requests


def create_audio(kanji, reading):

    kanji =kanji.encode("utf-8")
    reading = reading.encode("utf-8")

    reading = urllib.parse.quote(reading)
    kanji = urllib.parse.quote(kanji)

    try:
        url = f"http://assets.languagepod101.com/dictionary/japanese/audiomp3.php?kana={reading}&kanji={kanji}"

        audio_file = requests.get(url)

        open(kanji+".mp3","wb").write(audio_file.content)
    except TypeError as e:
        raise e


if __name__ == '__main__':
    kanji = input("Input the kanji: ")
    reading = input("Input the hiragana: ")
    create_audio(kanji, reading)
