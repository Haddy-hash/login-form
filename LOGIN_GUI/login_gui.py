import tkinter
from tkinter import *


#Colors
color1="gray"
color2="black"
color3="white"

#Root
master=Tk()
master.minsize(1350, 730)

#Importing Icons and Button.
fb_icon=PhotoImage(file="flat\\facebook.png") 
pinterest_icon=PhotoImage(file="flat\\pinterest.png") 
instagram_icon=PhotoImage(file="flat\\instagram.png") 
twitter_icon=PhotoImage(file="flat\\twitter.png") 
twitter_button=PhotoImage(file="social_signin\\tweet.png") 
google_button=PhotoImage(file="social_signin\\google.png") 
facebook_button=PhotoImage(file="social_signin\\facebook.png") 
login_button=PhotoImage(file="gradient_icons\\login.png") 

#Background Images
bkg_image=PhotoImage(file="images\\dock.png")
login_image=PhotoImage(file="images\\login_bg.png")

main_bg=Label(master, image=bkg_image)
main_bg.pack()

login_bg=Label(main_bg, image=login_image, bd=0)
login_bg.place(x=95, y=40)

login_frame=Frame(login_bg, bg=color3, height=600, width=400)
login_frame.place(x=40, y=20)
social_login=Frame(login_bg, bg=color3, height=600, width=400)
social_login.place(x=490, y=20)
or_label=Label(login_bg, bg=color3, text="OR", font=("Comic Sans Ms", 20, "bold"))
or_label.place(x=440, y=250)

login_info=Label(login_frame, text="Login to your TribeX account", bg=color3, font=("Comic Sans Ms", 15, "bold"))
login_info.place(x=50, y=60)
email_label=Label(login_frame, text="USERNAME", bg=color3, fg=color2, font=("Comic Sans Ms", 10, "bold"))
email_label.place(x=50, y=150)
email_entry=Entry(login_frame, relief="flat", width=37, fg=color2, font=("Comic Sans Ms", 10, "bold"))
email_entry.place(x=50, y=180)
email_line=Frame(login_frame, height=2, width=300)
email_line.place(x=50, y=200)

pass_label=Label(login_frame, text="PASSWORD", bg=color3, fg=color2, font=("Comic Sans Ms", 10, "bold"))
pass_label.place(x=50, y=220)
pass_entry=Entry(login_frame, relief="flat", width=37, fg=color1, font=("Comic Sans Ms", 10, "bold"), show="*")
pass_entry.place(x=50, y=250)
pass_line=Frame(login_frame, height=2, width=300)
pass_line.place(x=50, y=270)

rem_box=Checkbutton(login_frame, bg=color3, state="normal", relief="flat")
rem_box.place(x=200, y=280)
rem_label=Label(login_frame, bg=color3, text="Remember me", font=("Comic Sans Ms", 10))
rem_label.place(x=220, y=280)

login_btn=Button(login_frame, bg=color3, image=login_button, bd=0, relief="flat")
login_btn.place(x=100, y=320)

share_frame=Frame(login_frame, bg=color3, height=50, width=500)
share_frame.place(x=0, y=380)
margin=Label(share_frame, bg=color3, width=12)
margin.pack(side=LEFT)
fb_ico=Button(share_frame, bg=color3, image=fb_icon, bd=0, relief="flat")
fb_ico.pack(side=RIGHT)
margin=Label(share_frame, bg=color3, width=3)
margin.pack(side=RIGHT)
twitter_ico=Button(share_frame, bg=color3, image=twitter_icon, bd=0, relief="flat")
twitter_ico.pack(side=RIGHT)
margin=Label(share_frame, bg=color3, width=3)
margin.pack(side=RIGHT)
instagram_ico=Button(share_frame, bg=color3, image=instagram_icon, bd=0, relief="flat")
instagram_ico.pack(side=RIGHT)
margin=Label(share_frame, bg=color3, width=3)
margin.pack(side=RIGHT)
pinterest_ico=Button(share_frame, bg=color3, image=pinterest_icon, bd=0, relief="flat")
pinterest_ico.pack(side=RIGHT)

social_label=Label(social_login, text="Sign in with Social media", bg=color3, font=("Comic Sans Ms", 15, "bold"))
social_label.place(x=10, y=120)
tweet_btn=Button(social_login, bg=color3, image=twitter_button, bd=0, relief="flat")
tweet_btn.place(x=30, y=190)
google_btn=Button(social_login, bg=color3, image=google_button, bd=0, relief="flat")
google_btn.place(x=70, y=240)
facebook_btn=Button(social_login, bg=color3, image=facebook_button, bd=0, relief="flat")
facebook_btn.place(x=110, y=290)

master.mainloop()