from pytube import YouTube,Playlist   #python -m pip install git+https://github.com/nficano/pytube
from os import system,name
import os
import sys
from pytube.cli import on_progress
from time import sleep
import pyfiglet 
#cwd = os.getcwd()
uname=os.getenv('username')
cwd="C:/Users/{}/Downloads/".format(uname)
banner = pyfiglet.figlet_format("YTD", font = "alligator" ) 
def clear(): 
	'''Frame Change'''
	# for windows 
	if name == 'nt':
		_ = system('cls')   
	# for linux 
	else: 
		_ = system('clear')
	print(banner)
	print("\t-by VAIBHAV HASWANI\n")

def video_download(link):
	'''Video Download Function'''
	clear()
	try:
		yt_obj=YouTube(link,on_progress_callback=on_progress)

		print(f"Video: '{yt_obj.title} by {yt_obj.author}'\n\nDescription:\n{yt_obj.description}\n")


		while True:
			typ=input('Download Type:\n1)Video\n2)Audio\n>')
			if typ=='1' or typ=='2':
				break
			else:
				print("...Invalid Choice Entered...")
		clear()
		
		if typ=='1':
			#If Downloading Video
			filters=yt_obj.streams.filter(progressive=True,file_extension='mp4')
			print("Available Formats:")
			for i,f in enumerate(filters):
				print(f"{i}> resolution:{f.resolution} fps:{f.fps}")
			i=input("Enter Format id (from above):")
			print(f'\n\nDownloading {yt_obj.title} with {filters[int(i)].resolution} resolution....')
			filters[int(i)].download(output_path=os.path.join(cwd,'ytdownloads/'))
			print(f"Video Download succeeded! (Check {os.path.join(cwd,'ytdownloads/')})")
			sleep(3)
			main()

		elif typ=='2':
			#If downloading Audio
			filters=yt_obj.streams.filter(only_audio=True)
			print("Available Formats:")
			for i,f in enumerate(filters):
				print(f"{i}> type:{f.mime_type} bitrate:{f.abr}")
			i=input("Enter Format id (from above):")
			print(f'\n\nDownloading {yt_obj.title} audio with {filters[int(i)].abr}')
			filters[int(i)].download(output_path=os.path.join(cwd,'ytdownloads/audios'))
			print(f"Audio Download succeeded! (Check {os.path.join(cwd,'ytdownloads/audios')})")
			sleep(3)
			main()



	except Exception as e:
		print("...Trouble in Connection/Link...")
		print(e)
		sys.exit()


def playlist_download(link):
	'''Download Playlist'''
	clear()
	try:
		p=Playlist(link)
		print(f"Playlist Title:{p.title}\n")
		#yielding first video details for resolution input
		for v in p.videos:
			filters=v.streams.filter(progressive=True,file_extension='mp4')
			print("Available Formats:")
			for i,f in enumerate(filters):
				print(f"{i}> resolution:{f.resolution} fps:{f.fps}")
			break
		i=input("Enter Format id (from above):")
		res=filters[int(i)].resolution
		title=p.title
		syms=['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
		for i in syms:
			#removing conflicting symbols from title
			if i in title:
				title=title.replace(i,'_')
		for v in p.videos:
			#iterating through each video and downloading the video of required resolution
			print(f">Downloading {v.title}")
			f=v.streams.filter(progressive=True,file_extension='mp4')
			for s in f:
				if s.resolution==res:
					vdo=s
			vdo.download(output_path=os.path.join(cwd,f"ytdownloads/{title}"))
		print(f"..Playlist Downloaded (Check {os.path.join(cwd,f'ytdownloads/{title}')})..")
		sleep(3)
		main()
	except Exception as e:
		print("...Trouble in Connection/Link...")
		print(e)
		sys.exit()	


def main():
	'''Main Func'''
	clear()
	print("1) Video Link\n2) Playlist Link")
	while(True):
		o=input("Enter Choice:")
		if o=='1' or o=='2':
			break
		else:
			print("...Invalid Choice Entered...")

	clear()
	link=input("Enter Link:")
	#Calling desired function according to user input
	if o=='1':
		video_download(link)
	elif o=='2':
		playlist_download(link)


if __name__ == '__main__':
	main()

