# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "d:/path to video file/" #to_do

# link of the video to be downloaded
link=input("*** Please Enter Your Link ***\n")

try:
	# object creation using YouTube
	# which was imported in the beginning
	yt = YouTube(link)
except:
	print("Connection Error") #to handle exception

stream=yt.streams.first()


try:
	# downloading the video
	stream.download(SAVE_PATH)
except:
	print("Some Error!")
print('\nHurray!video was successfully downloaded')
