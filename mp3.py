from os import access, replace
from tkinter import *
import pygame
from pygame import mixer, mixer_music
from tkinter import filedialog
master= Tk()
master.title("Mp3 playter")
master.geometry("500x300")

# sond menu
def add_song ():
    song = filedialog.askopenfilename(initialdir="/home/balaji/Music",filetypes=(("mp3 files","*.mp3"),))
    song=song.replace("/home/balaji/Music/", "")
    song=song.replace(".mp3", "")
    music_box.insert(END,song)

def play():
    song = music_box.get(ACTIVE)
    song=f'/home/balaji/Music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    

# creating listbox
music_box=Listbox(master,background="black",foreground="red",width=60)
music_box.grid(pady=20)
# initiate pygames
pygame.mixer.init()
# find the image file directory
reverse_button_img =PhotoImage(file="/home/balaji/Pictures/reverse.png")
stop_button_img=PhotoImage(file="/home/balaji/Pictures/stop.png")
play_button_img=PhotoImage(file="/home/balaji/Pictures/play.png")
pause_button_img=PhotoImage(file="/home/balaji/Pictures/pause.png")
forward_button_img =PhotoImage(file="/home/balaji/Pictures/forward.png")

# creating control frame
control_frame=Frame(master)
control_frame.grid()
#creating image as a button
reverse_button = Button(control_frame,image=reverse_button_img,borderwidth=0)
stop_button= Button(control_frame,image=stop_button_img,borderwidth=0)
play_button= Button(control_frame,image=play_button_img,borderwidth=0, command=play)
pause_button= Button(control_frame,image=pause_button_img,borderwidth=0)
forward_button= Button(control_frame,image=forward_button_img,borderwidth=0)
# givind position to the image button
reverse_button.grid(row=0,column=0)
stop_button.grid(row=0,column=1)
play_button.grid(row=0,column=2)
pause_button.grid(row=0,column=3)
forward_button.grid(row=0,column=4,)

# create menu
my_menu=Menu(master)
master.config(menu=my_menu)
# adding menu for add songs
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Add song", command=add_song ,menu= add_song_menu)
add_song_menu.add_command(label="Add one song", command=add_song)

master.mainloop()