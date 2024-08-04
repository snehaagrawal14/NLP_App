from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:
    
    def __init__(self):
        self.dbo = Database() 
        self.apio = API()

        self.root = Tk()     # to create gui
        self.root.title("NLP App")        #to change the title of the window
        self.root.iconbitmap("resources/favicon.ico") #to change the icon(only ico format is supported)
        self.root.geometry('400x550') #to change the geometry(height and width) of the window
        self.root.configure(bg="#E8DAEF")   #to change the configuartion(like bg color) of the window
        self.login_gui()
        self.root.mainloop()     # to hold gui at screen
        
    def login_gui(self):
        self.clear()
        
        heading = Label(self.root, text = "NLP App", bg="#E8DAEF", fg="#4A235A")  #to create the heading or anyy text in the window
        heading.pack(pady=(30,30))  # for exciplicitly tell the tkinter to set the heading(this pack always place the text at the centre)
        heading.configure(font=("verdana", 24, 'bold'))   # to change the font
        
        label1 = Label(self.root, text = "Enter Email:", bg="#E8DAEF", fg="#4A235A")
        label1.pack(pady=(5,10))
        label1.configure(font=10)
        
        self.email_input = Entry(self.root, width = 40)
        self.email_input.pack(ipady = 5)
        
        label2 = Label(self.root, text = "Enter Password:", bg="#E8DAEF", fg="#4A235A")
        label2.pack(pady=(10,10))
        label2.configure(font=10)
        
        self.password_input = Entry(self.root, width = 40, show="*")
        self.password_input.pack(ipady = 5)
        
        login_btn = Button(self.root, text = "Login", bg="#4A235A", fg="white", width = 20, height = 1, font = 10, command=self.perform_login)
        login_btn.pack(pady = (25,10))
        
        label3 = Label(self.root, text = "Not a member?", bg="#E8DAEF", fg="#4A235A")
        label3.pack(pady=(10,10))
        label3.configure(font=5)
        
        redirect_btn = Button(self.root, text = "Register Now", bg="#4A235A", fg="white", command=self.register_gui)
        redirect_btn.pack(pady = (2,10))
        
    def register_gui(self):
        self.clear()
        
        heading = Label(self.root, text = "NLP App", bg="#E8DAEF", fg="#4A235A")  #to create the heading or anyy text in the window
        heading.pack(pady=(30,30))  # for exciplicitly tell the tkinter to set the heading(this pack always place the text at the centre)
        heading.configure(font=("verdana", 24, 'bold'))   # to change the font
        
        label0 = Label(self.root, text = "Enter Name:", bg="#E8DAEF", fg="#4A235A")
        label0.pack(pady=(5,10))
        label0.configure(font=10)
        
        self.name_input = Entry(self.root, width = 40)
        self.name_input.pack(ipady = 5)
        
        label1 = Label(self.root, text = "Enter Email:", bg="#E8DAEF", fg="#4A235A")
        label1.pack(pady=(5,10))
        label1.configure(font=10)
        
        self.email_input = Entry(self.root, width = 40)
        self.email_input.pack(ipady = 5)
        
        label2 = Label(self.root, text = "Enter Password:", bg="#E8DAEF", fg="#4A235A")
        label2.pack(pady=(5,10))
        label2.configure(font=10)
        
        self.password_input = Entry(self.root, width = 40, show="*")
        self.password_input.pack(ipady = 5)
        
        register_btn = Button(self.root, text = "Register", bg="#4A235A", fg="white", width = 20, height = 1, font = 10, command=self.perform_registration)
        register_btn.pack(pady = (15,10))
        
        label3 = Label(self.root, text = "Already a member?", bg="#E8DAEF", fg="#4A235A")
        label3.pack(pady=(5,5))
        label3.configure(font=10)
        
        redirect_btn = Button(self.root, text = "Login Now", bg="#4A235A", fg="white", command=self.login_gui)
        redirect_btn.pack(pady = (2,10))
        
    def clear(self):
        # clear existing gui
        for i in self.root.pack_slaves():
            i.destroy()
            
    def perform_registration(self):
        # fetch data from gui
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        
        response = self.dbo.add_data(name, email, password)
        
        if response:
            messagebox.showinfo("Success", "Registration successful. You can Login now.")
        else:
            messagebox.showerror("Error","Email already exists")
            
    def perform_login(self):
        # fetch data from gui
        email = self.email_input.get()
        password = self.password_input.get()
        
        response = self.dbo.search(email, password)
        if response == -1:
            messagebox.showerror("Error","Email not found.")
        elif response == 1:
            messagebox.showinfo("Success", "Login Success.")
            self.home_gui()
        else:
            messagebox.showerror("Error","Wrong Password")
            
    def home_gui(self):
        self.clear()

        heading = Label(self.root, text = "NLP App", bg="#E8DAEF", fg="#4A235A")  #to create the heading or anyy text in the window
        heading.pack(pady=(30,0))  # for exciplicitly tell the tkinter to set the heading(this pack always place the text at the centre)
        heading.configure(font=("verdana", 24, 'bold'))
        
        sentiment_btn = Button(self.root, text = "Sentiment Analysis", bg="#4A235A", fg="white", width = 20, height = 2, font = 10, command=self.sentiment_gui)
        sentiment_btn.pack(pady = (50,30))
        
        ner_btn = Button(self.root, text = "NER (Entity Extraction)", bg="#4A235A", fg="white", width = 20, height = 2, font = 10, command = self.ner_gui)
        ner_btn.pack(pady = (30,30))
        
        emotion_btn = Button(self.root, text = "Emotion Prediction", bg="#4A235A", fg="white", width = 20, height = 2, font = 10, command = self.emotion_gui)
        emotion_btn.pack(pady = (30,30))
        
        logout_btn = Button(self.root, text = "Logout", bg="#4A235A", fg="white", height = 1, command=self.login_gui)
        logout_btn.pack(pady = (30,30))
        
    def sentiment_gui(self):
        self.clear()
        
        heading2 = Label(self.root, text = "Sentiment Analysis", bg="#E8DAEF", fg="#4A235A")
        heading2.pack(pady=(30,20))
        heading2.configure(font=("verdana", 20, 'bold'))
        
        label1 = Label(self.root, text = "Enter text:", bg="#E8DAEF", fg="#4A235A", font = 1)
        label1.pack(pady=(10,15))
        
        self.sentiment_input = Entry(self.root, width = 40)
        self.sentiment_input.pack(ipady = 5)
        
        sentiment_btn = Button(self.root, text = "Analyze Sentiment", bg="#4A235A", fg="white", width = 20, height = 1, font = 10, command = self.do_sentiment_analysis)
        sentiment_btn.pack(pady = (30,30))
        
        self.sentiment_result = Label(self.root, text = "", bg="#E8DAEF", fg="#4A235A")
        self.sentiment_result.pack(ipady = 4)
        
        home_btn = Button(self.root, text = "Go Back", bg="#4A235A", fg="white", height = 1, command=self.home_gui)
        home_btn.pack(pady = (30,30))

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)
        
        output = ""
        for i in result:
            output += i["sentiment"] + " -> " + str(i["sentiment_rate"]) + "\n"

        self.sentiment_result["text"] = output

    def ner_gui(self):
        self.clear()
        
        heading2 = Label(self.root, text = "NER (Entity Extraction)", bg="#E8DAEF", fg="#4A235A")
        heading2.pack(pady=(30,10))
        heading2.configure(font=("verdana", 20, 'bold'))
        
        label1 = Label(self.root, text = "Enter text:", bg="#E8DAEF", fg="#4A235A", font = 1)
        label1.pack(pady=(10,15))
        
        self.ner_input = Entry(self.root, width = 40)
        self.ner_input.pack(ipady = 5)
        
        ner_btn = Button(self.root, text = "Analyze NER", bg="#4A235A", fg="white", width = 20, height = 1, font = 10, command = self.do_ner)
        ner_btn.pack(pady = (30,30))
        
        self.ner_result = Label(self.root, text = "", bg="#E8DAEF", fg="#4A235A")
        self.ner_result.pack(ipady = 5)
        
        home_btn = Button(self.root, text = "Go Back", bg="#4A235A", fg="white", height = 1, command=self.home_gui)
        home_btn.pack(pady = (30,30))

    def do_ner(self):
        text = self.ner_input.get()
        result = self.apio.ner(text)
        
        output = ""
        for i in result:
            for j in i:
                output += j+ " -> " + str(i[j]) + "\n"

        self.ner_result["text"] = output
        
    def emotion_gui(self):
        self.clear()
        
        heading2 = Label(self.root, text = "Emotion Anyalsis", bg="#E8DAEF", fg="#4A235A")
        heading2.pack(pady=(30,10))
        heading2.configure(font=("verdana", 20, 'bold'))
        
        label1 = Label(self.root, text = "Enter text:", bg="#E8DAEF", fg="#4A235A", font = 1)
        label1.pack(pady=(10,15))
        
        self.emotion_input = Entry(self.root, width = 40)
        self.emotion_input.pack(ipady = 5)
        
        emotion_btn = Button(self.root, text = "Analyze Emotion", bg="#4A235A", fg="white", width = 20, height = 1, font = 10, command = self.do_emotion)
        emotion_btn.pack(pady = (30,30))
        
        self.emotion_result = Label(self.root, text = "", bg="#E8DAEF", fg="#4A235A")
        self.emotion_result.pack(ipady = 5)
        
        home_btn = Button(self.root, text = "Go Back", bg="#4A235A", fg="white", height = 1, command=self.home_gui)
        home_btn.pack(pady = (30,30))

    def do_emotion(self):
        text = self.emotion_input.get()
        result = self.apio.emotion_analysis(text)
        
        output = ""
        for i in result:
            output += i["emotion"] + " -> " + str(i["emotion_score"]) + "\n"

        self.emotion_result["text"] = output

nlp = NLPApp() # to create object