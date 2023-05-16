import tkinter as tk
from PIL import Image, ImageTk
import webbrowser

class login:
    def __init__(self, root):
        self.root=root
        self.root.title('Entertain yourself')
        self.root.geometry('500x300+100+50')
        self.root.resizable(False, False)
        
        #background image
        image=Image.open('bg-image.jpeg')
        self.root.bg_image=ImageTk.PhotoImage(image)
        self.root.label=tk.Label(image=self.root.bg_image).pack(fill='both', expand=True, anchor='nw')
        
        self.root.label=tk.Label(text='Log in', font='ar 18 bold').place(x=200, y=0)
        self.root.f_name=tk.Label(text='Firt Name:').place(x=150, y=50)
        f_name_entry=tk.StringVar
        self.root.f_name_entry=tk.Entry(textvariable=f_name_entry).place(x=250, y=50)
        self.root.s_name=tk.Label(text='Last Name:').place(x=150, y=100)
        s_name_entry=tk.StringVar
        self.root.s_name_entry=tk.Entry(textvariable=s_name_entry).place(x=250, y=100)
        self.root.email=tk.Label(text='Email:').place(x=150, y=150)
        email_entry=tk.StringVar
        self.root.email_entry=tk.Entry(textvariable=email_entry).place(x=250, y=150)
        self.root.password=tk.Label(text='Password:').place(x=150, y=200)
        password_entry=tk.StringVar()
        self.root.password_entry=tk.Entry(show='*',textvariable=password_entry).place(x=250, y=200)
        
        def hide_password():
            self.root.password_entry=tk.Entry(show='*',textvariable=password_entry).place(x=250, y=200)
            self.root.show_password_button=tk.Button(text='Show',  command=show_password).place(x=400, y=200)


        def show_password():
            self.root.password_entry=tk.Entry(textvariable=password_entry).place(x=250, y=200)
            self.root.show_password_button=tk.Button(text=' Hide', command=hide_password).place(x=400, y=200)
                
        self.root.show_password_button=tk.Button(text='Show',  command=show_password).place(x=400, y=200)

        def submodule():
            root=tk.Tk()
            root.geometry('1199x600+100+50')
            root.title('country page')

            image2=Image.open('bg-image.jpeg')
            root.bg_image2=ImageTk.PhotoImage(image2)
            root.label=tk.Label(image=root.bg_image2).pack(fill=tk.BOTH, expand=True)

            tk.Label(root, text='Choose a country of your liking', font='ar 12 bold').grid(row=0, column=3)
            kenya=tk.StringVar
            def kenyan_artist():
               root=tk.Tk()
               root.geometry('1199x600+100+50')
               root.title('Kenyan Genras')
               kenyan_music=tk.StringVar
               tk.Button(root, text='Kenyan Music    ', textvariable=kenyan_music).grid(row=1, column=1)

               kenyan_comedyanddrama=tk.StringVar
               def comedy_and_drama():
                   root=tk.Tk()
                   root.geometry('1199x600+100+50')
                   root.title('Comedy And Drama')
                   '''comedy_and_drama_frame=tk.Frame(root).pack(side='right', fill=tk.BOTH, expand=True)
                   comedy_and_drama_listbox=tk.Listbox(comedy_and_drama_frame, font=('Aerial', 12)).pack(side='right', fill=tk.BOTH, expand=True)

                   scrollbar=tk.Scrollbar(comedy_and_drama_frame, orient=tk.VERTICAL, command=comedy_and_drama_listbox.yview).place(relx=1, rely=0, relheight=1, anchor='ne')
                   comedy_and_drama_listbox.config(yscrollcommand=scrollbar.set)
                   comedy_and_drama_listbox.bind("<<ListboxSelect>>", comedy_and_drama)
                   '''
                   tk.Label(root, text='Crazy Kenner', font='TimesNewRoman 15 italic bold').grid(row=3, column=3)
                   crazy_kenner_tiktok=tk.StringVar
                   def crazykenner_tiktok():
                        kenner_tt_url=''
                        webbrowser.open(kenner_tt_url)
                   tk.Button(root, text='TikTok', font='ar 12', textvariable=crazy_kenner_tiktok, command=crazykenner_tiktok).grid(row=4, column=3)

                   crazy_kenner_youtube=tk.StringVar
                   def crazykenner_youtube():
                        kenner_yt_url='https://youtube.com/@TalesofthecrazyKennar'
                        webbrowser.open(kenner_yt_url)
                   tk.Button(root, text='Youtube', font='ar 12', textvariable=crazy_kenner_youtube, command=crazykenner_youtube).grid(row=5, column=3)
                    
                   crazy_kenner_instagram=tk.StringVar
                   def crazykenner_instagram():
                        kenner_ig_url=''
                        webbrowser.open(kenner_ig_url)
                   tk.Button(root, text='Instagram', font='ar 12', textvariable=crazy_kenner_instagram, command=crazykenner_instagram).grid(row=6, column=3)
                   
                   #Rald Comedy
                   tk.Label(root, text='Rald Comedy', font='TimesNewRoman 15 italic bold').grid(row=8, column=3)
                   rald_comedy_tiktok=tk.StringVar
                   def raldcomedy_tiktok():
                       rald_tt_url=''
                       webbrowser.open(rald_tt_url)
                   tk.Button(root, text='TikTok', font='ar 12', textvariable=rald_comedy_tiktok, command=raldcomedy_tiktok).grid(row=9, column=3)

                   rald_comedy_youtube=tk.StringVar
                   def raldcomedy_youtube():
                       rald_yt_url='https://youtube.com/@raldcomedy'
                       webbrowser.open(rald_yt_url)
                   tk.Button(root, text='Youtube', font='ar 12', textvariable=rald_comedy_youtube, command=raldcomedy_youtube).grid(row=10, column=3)

                   rald_comedy_instagram=tk.StringVar
                   def raldcomedy_instagram():
                       rald_ig_url=''
                       webbrowser.open(rald_ig_url)
                   tk.Button(root, text='Instagram', font='ar 12', textvariable=rald_comedy_instagram, command=raldcomedy_instagram).grid(row=11, column=3)
                   
                   #Flaqo Raz
                   tk.Label(root, text='Flaqo Raz', font='TimesNewRoman 15 italic bold').grid(row=13, column=3)
                   flaqoraz_tiktok=tk.StringVar
                   def flaqoraz_tiktok_channel():
                       flaqo_tt_url=''
                       webbrowser.open(flaqo_tt_url)
                   tk.Button(root, text='TikTok', font='ar 12', textvariable=flaqoraz_tiktok, command=flaqoraz_tiktok_channel).grid(row=14, column=3)

                   flaqoraz_youtube=tk.StringVar
                   def flaqoraz_youtube_channel():
                       flaqo_yt_url='https://youtube.com/@flaqo'
                       webbrowser.open(flaqo_yt_url)
                   tk.Button(root, text='Youtube', font='ar 12', textvariable=flaqoraz_youtube, command=flaqoraz_youtube_channel).grid(row=15, column=3)

                   flaqoraz_instagram=tk.StringVar
                   def flaqoraz_instagram_channel():
                       flaqo_ig_url=''
                       webbrowser.open(flaqo_ig_url)
                   tk.Button(root, text='Instagram', font='ar 12', textvariable=flaqoraz_instagram, command=flaqoraz_instagram_channel).grid(row=16, column=3)

                   #Wololo Tv
                   tk.Label(root, text='Wololo Tv', font='TimesNewRoman 15 italic bold').grid(row=18, column=3)
                   wololo_tv_tiktok=tk.StringVar
                   def wololotv_tiktok_channel():
                       wololo_tt_url=''
                       webbrowser.open(wololo_tt_url)
                   tk.Button(root, text='TikTok', font='ar 12', textvariable=wololo_tv_tiktok, command=wololotv_tiktok_channel).grid(row=19, column=3)

                   wololo_tv_youtube=tk.StringVar
                   def wololotv_youtube_channel():
                       wololo_yt_url=''
                       webbrowser.open(wololo_yt_url)
                   tk.Button(root, text='Youtube', font='ar 12', textvariable=wololo_tv_youtube, command=wololotv_youtube_channel).grid(row=20, column=3)

                   wololo_tv_instagram=tk.StringVar
                   def wololotv_instagram_channel():
                       wololo_ig_url=''
                       webbrowser.open(wololo_ig_url)
                   tk.Button(root, text='Instagram', font='ar 12', textvariable=wololo_tv_instagram, command=wololotv_instagram_channel).grid(row=21, column=3)  
                   
                   #njugush 
                   tk.Label(root, text='Njugush Comedy', font='TimesNewRoman 15 italic bold').grid(row=23, column=3)
                   njugush_tiktok=tk.StringVar
                   def njugush_tiktok_channel():
                       njugush_tt_url=''
                       webbrowser.open(njugush_tt_url)
                   tk.Button(root, text='TikTok', font='ar 12', textvariable=njugush_tiktok, command=njugush_tiktok_channel).grid(row=24, column=3)

                   njugush_youtube=tk.StringVar
                   def njugush_youtube_channel():
                       njugush_yt_url=''
                       webbrowser.open(njugush_yt_url)
                   tk.Button(root, text='Youtube', font='ar 12', textvariable=njugush_youtube, command=njugush_youtube_channel).grid(row=25, column=3)

                   njugush_instagram=tk.StringVar
                   def njugush_instagram_channel():
                       njugush_ig_url=''
                       webbrowser.open(njugush_ig_url)
                   tk.Button(root, text='Instagram', font='ar 12', textvariable=njugush_instagram, command=njugush_instagram_channel).grid(row=26, column=3)
                   
               tk.Button(root, text='Kenyan Comedy', textvariable=kenyan_comedyanddrama, command=comedy_and_drama).grid(row=2, column=1)
               kenyan_blogs=tk.StringVar
               tk.Button(root, text='Kenyan Blogs      ', textvariable=kenyan_blogs).grid(row=3, column=1)
               
            btn=tk.Button(root, text='Kenya', textvariable=kenya, command=kenyan_artist).grid(row=1, column=2)

            #NIGERIA
            nigeria=tk.StringVar
            def nigerian_artist():
                root=tk.Tk()
                root.geometry('1199x600+100+50')
                root.title('Nigerian Genre')
            
            tk.Button(root, text='Nigeria', textvariable=nigeria, command=nigerian_artist).grid(row=2, column=2)

            #UGANDA
            uganda=tk.StringVar
            def ugandan_artist():
                root=tk.Tk()
                root.geometry('1199x600+100+50')
                root.title('Ugandan Genre')

            tk.Button(root, text='Uganda', textvariable=uganda, command=ugandan_artist).grid(row=3, column=2)

        check_value=tk.IntVar
        self.root.check_value_button=tk.Checkbutton(text='Submit', variable=check_value, command=submodule).place(x=250, y=250)
        
root=tk.Tk()
obj=login(root)
root.mainloop()