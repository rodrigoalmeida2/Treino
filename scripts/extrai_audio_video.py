import subprocess
# Extrai o áudio do vídeo
def extrai_audio(video_path, audio_output_path):
    """Extrai o áudio de um vídeo usando FFmpeg"""
    comando = f"ffmpeg -i {video_path} -q:a 0 -map a {audio_output_path}"
    subprocess.run(comando, shell=True)


if __name__=="__main__":
    video = ""
    outuput = ""
    try:
        extrai_audio(video, outuput)
    except ValueError as e:
        print(f"Error:{e}")
