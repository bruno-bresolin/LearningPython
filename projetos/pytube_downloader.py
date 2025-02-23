from tkinter import *
from yt_dlp import YoutubeDL
import os

# tkinter
root = Tk()
root.title("Youtube Downloader")
root.geometry("400x500")
root.resizable(False, False)

frame = Frame(root, padx=20, pady=40)  # Frame com padding
frame.pack()

# extrair url
url = Entry(frame, width= 30)
url.pack()
url.insert(0, "")


# função downloader
def downloader_youtube():
    try:
        # 1️⃣ Pega a URL digitada
        download_url = url.get()

        download_path = os.path.join(os.path.expanduser("~"), "Downloads")

        # 3️⃣ Configurações do yt-dlp para salvar na pasta Downloads
        ydl_opts = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Salva com o título do vídeo
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([download_url])

    except Exception as e:
        print(f"Erro: {e}")



button = Button(frame, text="Download", command=downloader_youtube, width=27, height=2)
button.pack(pady=10)








#mainloop
root.mainloop()