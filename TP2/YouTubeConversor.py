from pytube import YouTube
from functools import partial
from UI_constructors import UI_root
from tkinter import ttk
import tkinter as tk
import os

def download_file(link, column_num, row_num, file_type):
    try:
        yt = YouTube(link.get())
        #streams_mp4 = yt.streams.filter(file_extension='mp4', res=res)
        print('Link found')
        match file_type:
            case 'mp4':
                file = yt.streams.get_highest_resolution()
            case 'mp3':
                file = yt.streams.get_audio_only()
        print('Stream decoded')
        file_name = yt.title + '.' + file_type
        download_path = os.path.join(os.getcwd(), file_type)
        print('File being downloaded')
        file.download(output_path=download_path, filename=file_name)
        ttk.Label(ui.mainframe, text=f"The video: '{yt.title}' has finished downloading as an {file_type}").grid(column=column_num, row=row_num, sticky=tk.W)
    except:
        ttk.Label(ui.mainframe, text=f"ERROR. The link: '{link.get()}' is not a valid link").grid(column=column_num, row=row_num, sticky=tk.W)

ui = UI_root("YouTube Converter")
column_num, row_num = 0, 0
label = ttk.Label(ui.mainframe, text="Paste the youtube video URL: ").grid(column=column_num, row=row_num, sticky=tk.W)
link = tk.StringVar()
entry = ttk.Entry(ui.mainframe, width=100, textvariable=link)
entry.grid(column=column_num+1, row=row_num, sticky=(tk.E))
row_num += 1
download_mp4 = ttk.Button(ui.mainframe, text="Download file as mp4", command=partial(download_file, link, column_num+1, row_num, 'mp4')).grid(column=column_num, row=row_num, sticky=tk.W)
row_num += 1
download_mp4 = ttk.Button(ui.mainframe, text="Download file as mp3", command=partial(download_file, link, column_num+1, row_num, 'mp3')).grid(column=column_num, row=row_num, sticky=tk.W)
ui.root.mainloop()