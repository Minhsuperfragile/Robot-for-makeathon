from moviepy.editor import *
import pygame
# currently doesn't have that video below uploaded
clip = VideoFileClip('assets/introVideo.mp4')
clip = clip.subclip(0,10)
clip = clip.set_fps(24)
clip.preview()
pygame.quit()
