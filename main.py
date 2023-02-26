from pytube import YouTube
import os

if __name__ == "__main__":

    def Download(link, base_clip_path=""):
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            if not os.path.exists(base_clip_path) & base_clip_path != "":
                os.makedirs(base_clip_path)

                youtubeObject.download(output_path= base_clip_path, filename="base_video")
                print("Download is completed successfully")
            else:
                print(f"No path specified, downloading to {os.getcwd()}")
                youtubeObject.download(output_path= base_clip_path, filename="base_video")
        except:
            print("An error has occurred")
    
    link = input("Enter the link: ")
    Download(link, "~/Desktop/Video")
