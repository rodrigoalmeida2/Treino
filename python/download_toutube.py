import yt_dlp

# Função para baixar o vídeo
def download_video(url, output_filename="video.mp4"):
    ydl_opts = {
        'format': 'best',  # Escolhe o formato de melhor qualidade
        'outtmpl': output_filename  # Nome do arquivo de saída
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# URL do vídeo que você quer baixar
video_url = "https://youtu.be/VrN_pbj2Kds"

# Baixar o vídeo
download_video(video_url)

print(f"Download concluído. O vídeo foi salvo como 'video.mp4'")
