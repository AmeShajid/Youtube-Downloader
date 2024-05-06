#input your youtube link and then it will downlaod the video for you and put it in the folder

#first pip install pytube
#then import pytybe and sys
from pytube import YouTube
from sys import argv

#argv will take everything after the file name and put it in the link variable
#argv 1 will be the link basically
#so set link to argv 1
# Check if a YouTube video URL is provided as a command-line argument
if len(argv) != 2:
    # Prompt the user to input the YouTube video URL
    link = input("Please input the YouTube video URL: ")
else:
    # Extract the YouTube video URL from the command-line argument
    link = argv[1]

#this is us creating the youtube object
youtube = YouTube(link)

#here this is getting some youtube information you can check adn make sure you are getting the right videos
print("Title: ", youtube.title)
print("Number of views: ", youtube.views)

#this is the stream that we are going to download the vidoe
#this will get the highest resolution video
youtube_download = youtube.streams.get_highest_resolution()

#this is where we will put the the youtube download in the folder
#also that is just the pathanme of where we want it located
youtube_download.download("/Users/ameshajid/Documents/VisualStudioCode/Youtube Downloader")

#once it is done it will print this for us to know its done
print("Download completed... ENJOY")



























