from pytube import YouTube

# Inserir a URL do vídeo
url = input("Insira a URL do vídeo: ")

# Criar um objeto YouTube
yt = YouTube(url)

# Selecionar a resolução desejada (720p neste caso)
stream = yt.streams.filter(
    progressive=True,
    file_extension='mp4').order_by('resolution').desc().first()

# Baixar o vídeo
try:
    stream.download()
    print("Download concluído!")
except Exception as e:
    print(f"Erro durante o download: {e}")
