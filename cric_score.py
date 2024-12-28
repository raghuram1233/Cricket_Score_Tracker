import tkinter as tk
from tkinter import *
from tkinter.constants import *
import requests
from bs4 import BeautifulSoup

type='test'


font=('unica one',10)

root=tk.Tk()
root.title("Cricket")
icon = tk.PhotoImage(file='img\\ball.png')
root.iconphoto(False,icon)
root.geometry('400x250')
root.config(bg='#0f0f0f')

frame1_1= tk.Frame(root,width=200,height=62,bg='#0f0f0f')
frame1_1.place(x=0,y=0)

frame1_2= tk.Frame(root,width=200,height=62,bg='#0f0f0f')
frame1_2.place(x=200,y=0)

frame2= tk.Frame(root,width=200,height=64,bg='#0f0f0f')
frame2.place(x=0,y=61)

frame3= tk.Frame(root,width=200,height=64,bg='#0f0f0f')
frame3.place(x=200,y=61)

frame4= tk.Frame(root,width=400,height=52,bg='#0f0f0f')
frame4.place(x=0,y=125)

frame5= tk.Frame(root,width=400,height=71,bg='#0f0f0f')
frame5.place(x=0,y=177)

tempframe1 = tk.Frame(frame2,bg='#0f0f0f')
tempframe1.place(relx=0.5,rely=0.5,anchor=CENTER)

tempframe2 = tk.Frame(frame3,bg='#0f0f0f')
tempframe2.place(relx=0.5,rely=0.5,anchor=CENTER)

match_btwn=tk.Label(frame1_1,fg='white',bg='#0f0f0f',font=font)

match_btwn.pack(padx=20,pady=20)


teamone_1innings=tk.Label(tempframe1,fg='white',bg='#0f0f0f',font=font)

teamone_1innings.pack()

teamone_2innings=tk.Label(tempframe1,fg='white',bg='#0f0f0f',font=font)

teamone_2innings.pack()

oversone=tk.Label(tempframe1,bg='#0f0f0f',fg='white',font=font)

oversone.pack()


teamtwo_1innings=tk.Label(tempframe2,bg='#0f0f0f',fg='white',font=font)

teamtwo_1innings.pack()

teamtwo_2innings=tk.Label(tempframe2,fg='white',bg='#0f0f0f',font=font)

teamtwo_2innings.pack()

overstwo=tk.Label(tempframe2,bg='#0f0f0f',fg='white',font=font)

overstwo.pack() 


stats = tk.Label(frame4,bg='#0f0f0f',fg='white',font=font)

stats.place(relx=.5, rely=.5,anchor= CENTER)

inning_stat = tk.Label(root,bg='#0f0f0f',fg='white',font=font)
inning_stat.pack(anchor=E,padx=80,pady=20)
 
root.update() 

def main():
    ent=tk.Entry(root)
    ent.place(x=120,y=115)
    match_btwn.config(text='')
    teamone_1innings.config(text='')
    teamone_2innings.config(text='')
    teamtwo_1innings.config(text='')
    teamtwo_2innings.config(text='')
    oversone.config(text='')
    overstwo.config(text='')
    stats.config(text='')
    inning_stat.config(text='')


    def test_update():
        URL=ent.get()
        ent.place_forget()
        btn.place_forget()

        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

        page = requests.get(URL,headers=headers)

        soup = BeautifulSoup(page.content,'html.parser')
        match_info=soup.find(class_='IkSHxd ellipsisize').get_text()


        teamone_score=[]
        teamtwo_score=[]

        try:
            score_one = soup.find(class_='imspo_mh_cricket__first-score imspo_mh_cricket__one-innings-column-with-overs')
            score=score_one.find(class_='imspo_mh_cricket__score-major').get_text()
            overs1=score_one.find(class_='imspo_mh_cricket__score-minor').get_text()
            oversone.config(text=overs1)
            teamone_1innings.config(text=score)

        except:
            pass

        try:
            score_one = soup.find(class_='imspo_mh_cricket__first-score imspo_mh_cricket__two-innings-column')
            for data in score_one.find_all(class_='imspo_mh_cricket__score-major'):
                teamone_score.append(data.get_text())

            #adding label
            teamone_1innings.config(text=teamone_score[0])
            teamone_2innings.config(text=teamone_score[1])
            try:
                overs1=score_one.find(class_='imspo_mh_cricket__score-minor').get_text()
                oversone.config(text=overs1)
            except:
                pass

        except:
            pass
        
        try:
            score_two = soup.find(class_='imspo_mh_cricket__second-score imspo_mh_cricket__one-innings-column-with-overs')
            score1=score_two.find(class_='imspo_mh_cricket__score-major').get_text()
            over2=score_two.find(class_='imspo_mh_cricket__score-minor').get_text()
            teamtwo_1innings.config(text=score1)
            overstwo.config(text=over2)

        except:
            pass

        try:
            score_two = soup.find(class_='imspo_mh_cricket__second-score imspo_mh_cricket__two-innings-column')
            for dat in score_two.find_all(class_='imspo_mh_cricket__score-major'):
                teamtwo_score.append(dat.get_text())

            #adding label
            teamtwo_1innings.config(text=teamtwo_score[0])
            teamtwo_2innings.config(text=teamtwo_score[1])
            try:
                overs1=score_one.find(class_='imspo_mh_cricket__score-minor').get_text()
                oversone.config(text=overs1)
            except:
                pass
        
        except:
            pass

        status = soup.find(class_='imso_mh__score-txt imso-ani imspo_mh_cricket__summary-sentence').get_text()
        try:
            innings = soup.find(class_='imso_mh__lv-m-stts-cont').get_text()
        except:
            innings = soup.find(class_='imso_mh__score-txt imso-ani imspo_mh_cricket__summary-sentence').get_text()
        inning_stat.config(text=innings)
        data=''
        dat=''

        match_btwn.config(text=match_info)
        stats.config(text=status)
        root.update()
        global lop
        lop=root.after(3000,test_update)
    if type=='test':
        btn = tk.Button(root,text='Enter',command=test_update)
        btn.place(x=255,y=112)

    #if type=='whiteball':
    #    btn = tk.Button(root,text='Enter',command=white_update)
    #    btn.place(x=255,y=112)

def restart():
    root.after_cancel(lop)
    main()

ref_img = tk.PhotoImage(file='img\\reload_img.png')
back_img = tk.PhotoImage(file='img\\back_img.png')

rebtn = tk.Button(frame1_2,image=ref_img,command=restart,bg='#0f0f0f',border=0,activebackground='#0f0f0f')
rebtn.pack(padx=150,pady=15)

backbtn = tk.Button(frame1_2,image=back_img,command=main,bg='#0f0f0f',border=0,activebackground='#0f0f0f')
backbtn.pack(padx=100,pady=15)

main()

root.mainloop()