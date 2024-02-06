from pytube import YouTube
from tkinter import filedialog
import tkinter as tk


def download_yt_video(url, save_path):
    try:
        yt = YouTube(url,
                     use_oauth=True,
                     allow_oauth_cache=True
                     )
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res_streams = streams.get_highest_resolution()
        highest_res_streams.download(
            output_path=save_path)
        print('Successfully downloaded the video!')
    except Exception as e:
        print(e)


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f'Selected folder: {folder}')
    else:
        return False
    return folder


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    url = input('Please enter a YouTube url: ')
    save_path = open_file_dialog()

    if save_path:
        download_yt_video(url, save_path)
    else:
        print('Provide valid save location!')
