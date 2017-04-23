from moviepy.editor import *
videofile = VideoFileClip("Video_File_Name.mp4")  
#^ Add the filename of the video 
videofile.audio.write_audiofile("Output_Audio_Filename.mp3")
#^ Add the filename of the output file.