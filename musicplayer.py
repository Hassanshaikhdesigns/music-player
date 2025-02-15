from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer

mixer.init()


########################################## FUNCTIONS ################################################

def start_music():
    print("music is playing")
    mixer.music.load("Glass Animals - Heat Waves (Official Video) (1).mp3")
    mixer.music.play()
    resume_btn.configure(text=" | | ")
    resume_btn.configure(command=pause_music)


def pause_music():
    print("music has paused")
    mixer.music.pause()
    resume_btn.configure(text=" ⏵ ")
    resume_btn.configure(command=unpause_music)


def unpause_music():
    mixer.music.unpause()
    resume_btn.configure(text=" | | ")
    resume_btn.configure(command=pause_music)






#####################################################################################

root = Tk()
root.title("Music Player")
root.geometry("400x550")
root.configure(bg="#1e1e2f")  # Dark background for a modern look


# Header
headlab = Label(
    root,
    text="Music Player",
    font=("Verdana", 18, "bold"),
    bg="#1e1e2f",
    fg="white",
)
headlab.pack(pady=20)


# Music Frame
musicframe = Frame(root, bg="#2a2a3b", bd=10, relief="ridge")
lab = Label(
    musicframe, text="Playing Now", bg="#2a2a3b", fg="white", font=("Verdana", 12)
)
lab.pack(side=BOTTOM, pady=(0, 10))

# Album image
img = Image.open("musicimg.png")
resimg = img.resize((200, 200))
newimg = ImageTk.PhotoImage(resimg)

labimg = Label(musicframe, image=newimg, bg="#2a2a3b")
labimg.pack(anchor=CENTER, pady=30)

musicframe.pack(pady=(10, 35))
musicframe.pack_propagate(False)
musicframe.configure(height=300, width=350)


# Control Buttons Frame
buttonframe = Frame(root, bg="#1e1e2f")


# Previous Button
prev_btn = Button(
    buttonframe,
    text="⏮",  # Unicode character for previous
    bg="#ff5e5e",
    fg="white",
    font=("Verdana", 17),
    bd=0,
    relief=GROOVE,
    command=unpause_music,
    width=3,
)
prev_btn.grid(row=0, column=0, padx=20, pady=10)

# Play/Pause Button
resume_btn = Button(
    buttonframe,
    text="⏵",  # Unicode character for play
    bg="#1cd1a1",
    fg="white",
    font=("Verdana", 17),
    bd=0,
    relief=GROOVE,
    width=3,
    command=start_music
)
resume_btn.grid(row=0, column=1, padx=20, pady=10)

# Next Button
next_btn = Button(
    buttonframe,
    text="⏭",  # Unicode character for next
    bg="#ff5e5e",
    fg="white",
    font=("Verdana", 17),
    bd=0,
    relief=GROOVE,
    width=3,
    command=pause_music
)
next_btn.grid(row=0, column=2, padx=20, pady=10)

buttonframe.pack(pady=10)




root.mainloop()