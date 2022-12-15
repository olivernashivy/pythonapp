import os
import shutil
#get pc username
username = os.getlogin()
#check if the os is windows , linux or mac
if os.name == "nt":
    #windows path
    download_path = "C:/Users/" + username + "/Downloads"

elif os.name == "posix":
    #linux path
    download_path = "/home/" + username + "/Downloads"
elif os.name == "mac":
    #mac path
    download_path = "/Users/" + username + "/Downloads"

# set the path to the directory you want to sort
path = download_path

# set the extensions types
image_extentions = [".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp", ".tiff", ".tif"]
video_extentions = [".mp4", ".mkv", ".avi", ".mov", ".webm", ".flv", ".wmv", ".mpeg", ".mpg"]
audio_extentions = [".mp3", ".wav", ".flac", ".ogg", ".wma", ".aac", ".m4a"]
document_extentions = [".doc", ".docx", ".pdf", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"]
compressed_extentions = [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"]
executable_extentions = [".exe", ".msi", ".deb", ".pkg", ".apk", ".dmg"]

# ctreate  directories
image_dir = download_path + "/Images"
video_dir = download_path + "/Videos"
audio_dir =download_path + "/Audios"
document_dir =download_path + "/Documents"
compressed_dir =download_path + "/Compressed"
executable_dir =download_path + "/Executables"

# create the directories inside download directory if they are not there
if not os.path.exists(image_dir):
    os.mkdir(image_dir)
    print("Created directory: " + image_dir)

if not os.path.exists(video_dir):
    os.mkdir(video_dir)
    print("Created directory: " + video_dir)

if not os.path.exists(audio_dir):
    os.mkdir(audio_dir)
    print("Created directory: " + audio_dir)

if not os.path.exists(document_dir):
    os.mkdir(document_dir)
    print("Created directory: " + document_dir)

if not os.path.exists(compressed_dir):
    os.mkdir(compressed_dir)
    print("Created directory: " + compressed_dir)

if not os.path.exists(executable_dir):
    os.mkdir(executable_dir)
    print("Created directory: " + executable_dir)


# loop through all the files in the directory
for file in os.listdir(path):
    # get the file name and extension
    file_name, file_extention = os.path.splitext(file)

    #  if the file is an image and move it to the image directory
    if file_extention in image_extentions:
        shutil.move(os.path.join(path, file), os.path.join(image_dir, file))

    # move it to the video directory
    elif file_extention in video_extentions:
        shutil.move(os.path.join(path, file), os.path.join(video_dir, file))

    # move it to the audio directory
    elif file_extention in audio_extentions:
        shutil.move(os.path.join(path, file), os.path.join(audio_dir, file))

    # move to the document directory
    elif file_extention in document_extentions:
        shutil.move(os.path.join(path, file), os.path.join(document_dir, file))

    #  move it to the compressed directory
    elif file_extention in compressed_extentions:
        shutil.move(os.path.join(path, file), os.path.join(compressed_dir, file))

    # move it to the executable directory
    elif file_extention in executable_extentions:
        shutil.move(os.path.join(path, file), os.path.join(executable_dir, file))
    

print("All files have been sorted successfully!")
