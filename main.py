from moviepy.editor import *

video = VideoFileClip("video.mp4")

video.audio.write_audiofile("audio.mp3")
