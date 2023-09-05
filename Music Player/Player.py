from tkinter import *
import pygame
from tkinter import filedialog


root= Tk()
root.title('Mp3 Player')
root.iconbitmap('')
root.geometry("500x300")



# initialize pygame mixer
pygame.mixer.init()

#Add Song fuction
def add_song():
    song= filedialog.askopenfilename(initialdir='',title="Choose a song",filetypes=(("mp3 files","*.mp3"), ))
    
    #Strip out the directory info and .mp3 extension form the song
    song=song.replace("","")
    song=song.replace(".mp3","")
    
    song_box.insert(END, song)
    
# Add many songs to playlist
def add_song_many():
    songs= filedialog.askopenfilenames(initialdir='',title="Choose a song",filetypes=(("mp3 files","*.mp3"), ))


    # loop thru song list replace directory info and mp3
    for song in songs:
        song=song.replace("","")
        song=song.replace(".mp3","")
        # Insert into playlist
        song_box.insert(END,song)
        

#Play selected song
def play():
    song=song_box.get(ACTIVE)
    song=f'{song}.mp3'
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    
# Stop Playing current song
def stop():
    pygame.mixer.music.stop()
    song_box.select_clear(ACTIVE)

# Play the next song in the playlist
def next_song():
    # Get the current song tuple number
    next_one = song_box.curselection()
    # Add one to the current song number
    next_one = next_one[0]+1
    #Grad song tiltle from playlist
    song = song_box.get(next_one)
    # Add directory structure and mp3 to title
    song=f'{song}.mp3'
    # Load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    
    # Move active bar in playlist listbox
    song_box.select_clear(0,END)

#Create Global pause variable
global paused
paused = False

# Pause and unpause the current song
def pause(is_paused):
    global paused
    paused=is_paused
    
    if paused:
         #Unpause
        pygame.mixer.music.unpause()
        paused=False
    else:
        #Pause 
        pygame.mixer.music.pause()
        paused=True
    
 


#create playlist box
song_box = Listbox(root, bg="white", fg="black",width=300, selectbackground="gray", selectforeground="black")
song_box.pack(pady=20)

#Define player control buttons images

play_btn=PhotoImage(file='player pics/play.png')
pause_btn=PhotoImage(file='player pics/pause.png')
stop_btn=PhotoImage(file='player pics/stop.png')
back_btn=PhotoImage(file='player pics/back.png')
Next_btn=PhotoImage(file='player pics/forward.png')

# Create player control frame
control_frame=Frame(root)
control_frame.pack()

#Create player control Button
back_button=Button(control_frame,image=back_btn,borderwidth=0)
play_button=Button(control_frame,image=play_btn,borderwidth=0,command=play)
puase_button=Button(control_frame,image=pause_btn,borderwidth=0,command=lambda: pause(paused))
stop_button=Button(control_frame,image=stop_btn,borderwidth=0,command=stop)
next_button=Button(control_frame,image=Next_btn,borderwidth=0, command=next_song)

back_button.grid(row=0,column=0,padx=5)
play_button.grid(row=0,column=2,padx=5)
puase_button.grid(row=0,column=1,padx=5)
stop_button.grid(row=0,column=3,padx=5)
next_button.grid(row=0,column=4,padx=5)

# create Menu
my_menu=Menu(root)
root.config(menu=my_menu)

#Add song menu
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Add Songs",menu=add_song_menu)
add_song_menu.add_command( label="Add one song to playlist", command=add_song)

# Add many Song to playlist
add_song_menu.add_command( label="Add many songs to playlist", command=add_song_many)

root.mainloop()