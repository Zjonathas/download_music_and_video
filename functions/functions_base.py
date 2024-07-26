from pytube import YouTube


def menu():
    while True:
        print("1. Download Video")
        print("2. Download Playlist")
        print("3. Download Audio")
        print("4. Sair")
        option = input("Choose an option: ")

        choices = {
            "1": download_video,
            "2": download_playlist,
            "3": download_audio,
            "4": exit
        }

        if option in choices:
            choices[option]()
        else:
            print("Invalid option")


def download_video():
    url = input("Insert the video URL: ")
    yt = YouTube(url)
    try:
        stream = yt.streams.filter(
            progressive=True,
            file_extension='mp4').order_by('resolution').desc().first().download() # noqa
        print("Download completed!")
    except Exception as e:
        print(f"Error during download: {e}")


def download_playlist():
    url = input("Insert the playlist URL: ")
    yt = YouTube(url)
    stream = yt.streams.filter(
        progressive=True,
        file_extension='mp4').order_by('resolution').desc().first()
    try:
        stream.download()
        print("Download completed!")
    except Exception as e:
        print(f"Error during download: {e}")


def download_audio():
    url = input("Insert the video URL: ")
    yt = YouTube(url)
    stream = yt.streams.filter(
        only_audio=True).first()
    try:
        stream.download()
        print("Download completed!")
    except Exception as e:
        print(f"Error during download: {e}")
