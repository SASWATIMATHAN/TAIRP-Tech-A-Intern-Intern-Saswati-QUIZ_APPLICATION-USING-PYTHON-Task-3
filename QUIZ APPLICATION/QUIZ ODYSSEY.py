# the json module to work with json files 
import json
import tkinter
from tkinter import *
import random


# questions = [
#     "India is a federal union comprising twenty-eight states and how many union territories?",
#     "Which of the following is the capital of Arunachal Pradesh?",
#     "What are the major languages spoken in Andhra Pradesh ?",
#     "What is the state flower of Haryana ?",
#     "In which of the following state, the main language is Khasi ?",
#     "Which is the largest coffee-producing state of India  ?",
#     "In what state is Elephant Falls located?",
#     "Which state of India celebrates Hunter Holi, an 800-year tradition ?",
#     "What is the staple drink of Goa ?",
#     "Who heads the RBI ?",
# ]

# answers_choice = [
#     ["6","7","8","9",],
#     ["Itanagar","Dispur","Imphal","Panaji",],
#     ["Odia and Telugu"," Telugu and Urdu","Telugu and Kannada","All of the above languages",],
#     ["Lotus","Rhododendron","Golden Shower","Not Declared",],
#     ["Mizoram","Nagaland","Meghalaya","Tripura",],
#     ["Kerala","Tamil Nadu","Karnataka"," Arunachal Pradesh",],
#     ["Mizoram","Orissa","Manipur","Meghalaya",],
#     ["Punjab","Haryana","Delhi","Uttar Pradesh",],
#     ["Toddy","Feni","Thandai","Sattu Sharbat",],
#     ["Urjit Patel","Raghuram Rajan","YV Reddy","Shaktikanta Das",],
# ] 

# load questions and answer choices from json file instead of the file
with open('./data.json', encoding="utf8") as f:
    data = json.load(f)

# convert the dictionary in lists of questions and answers_choice 
questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]

answers = [2,0,1,0,2,2,3,1,1,3] 

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes)< 5):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "#3EB489",
        border = 0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Arial Black",20),
        background = "#FF7F7F",
    )
    labelresulttext.pack()
    if score >= 20:
        img = PhotoImage(file="Great job.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Excellent! Kya baat, Kya baat, Kya baat!")
    elif (score >= 10 and score < 20):
        img = PhotoImage(file="Thumbs up.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Good try! Thoda aur accha ho sakta hai!")
    else:
        img = PhotoImage(file="Poor performance.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Fikar not! Better luck next time!")


def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)


ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        # print(indexes)
        # print(user_answer)
        # these two lines were just developement code
        # we don't need them
        calc()
    




def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(
        root,
        text = questions[indexes[0]],
        font = ("Arial black", 16),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#FF80FF",
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("Times", 12),
        value = 0,
        variable = radiovar,
        command = selected,
        background = "#90EE90",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][1],
        font = ("Times", 12),
        value = 1,
        variable = radiovar,
        command = selected,
        background = "#ADD8E6",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][2],
        font = ("Times", 12),
        value = 2,
        variable = radiovar,
        command = selected,
        background = "#FFD580",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][3],
        font = ("Times", 12),
        value = 3,
        variable = radiovar,
        command = selected,
        background = "#CBC3E3",
    )
    r4.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()



root = tkinter.Tk()
root.title("Quizstar")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)


img1 = PhotoImage(file="Welcome.png")

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(40,0))

labeltext = Label(
    root,
    text = "Quiz Odyssey",
    font = ("Georgia",34,"bold"),
   background = "#967bb6",
)
labeltext.pack(pady=(0,50))

img2 = PhotoImage(file="Start.png")

btnStart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command = startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text = "Review the Guidelines and Begin when Prepared",
    background = "#90E4C1",
    font = ("Bukhari Script",14, "bold"),
    justify = "center",
)
lblInstruction.pack(pady=(10,100))

lblRules = Label(
    root,
    text = "This quiz comprises 10 questions, each with a 20-second time limit.\nOnce you choose a radio button, your selection is final,\nso consider your options carefully before making a decision.",
    width = 100,
    font = ("Times",14),
    background = "#000000",
    foreground = "#FACA2F",
)
lblRules.pack()

root.mainloop()
