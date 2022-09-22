from tkinter import*
import random 
root =Tk()
root.title("lucky friend wheel")
root.geometry("500x500")
list1=["GFTEI","HJFDS","GFUDJ","HKSUD","BSGT"]
print(list1)

def random_number():
    random_no=random.randint(0,4)
    print(random_no)
    random_lucky_friend=list1[random_no]
    print("the word is: "+random_lucky_friend)

btn1=Button(root)
btn1=Button(root,text="GENERATE RANDOM WORDS ",command=random_number)
btn1.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()
