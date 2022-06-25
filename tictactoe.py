from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.title('TicTacToe')

Label(root,text  = "player1 : x",font="times 15").grid(row=0,column=1)

Label(root,text  = "player2 : o",font="times 15").grid(row=0,column=2)

digits = [1,2,3,4,5,6,7,8,9]

mark = ''

count= 0

panels = ["pannel"]*10

def win (panels,sign):
    return((panels [1]==panels[2]==panels[3]==sign )
    or(panels[1]==panels[4]==panels[7]==sign)
    or(panels[2]==panels[5]==panels[8]==sign)
    or(panels[1]==panels[5]==panels[9]==sign)
    or(panels[3]==panels[6]==panels[9]==sign)
    or(panels[3]==panels[5]==panels[7]==sign)
    or(panels[4]==panels[5]==panels[6]==sign)
    or(panels[7]==panels[8]==panels[9]==sign)
    )


def checker(digit):
 
    global count,mark,digits
    if digit==1 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark = 'x'
            panels[digit] = mark
        elif count%2!=0:
            mark = 'o'
            panels[digit] = mark
        btn1.config(text= mark)
        count = count+1
        sign=mark
        if (win(panels,sign) and sign == 'x'):
            msg.showinfo ("result","Player One Wins !!")
            root.destroy()
        elif (win(panels,sign) and sign == 'o'):
            msg.showinfo ("result","Player Two Wins !!")
            root.destroy()

    if digit==2 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark = 'x'
            panels[digit] = mark
        elif count%2!=0:
            mark = 'o'
            panels[digit] = mark
        btn2.config(text= mark)
        count = count+1
        sign=mark
        if (win(panels,sign) and sign == 'x'):
            msg.showinfo ("result","Player One Wins !!")
            root.destroy()
        elif (win(panels,sign) and sign == 'o'):
            msg.showinfo ("result","Player Two Wins !!")
            root.destroy()

    if digit==3 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark = 'x'
            panels[digit] = mark
        elif count%2!=0:
            mark = 'o'
            panels[digit] = mark
        btn3.config(text= mark)
        count = count+1
        sign=mark
        if (win(panels,sign) and sign == 'x'):
            msg.showinfo ("result","Player One Wins !!")
            root.destroy()
        elif (win(panels,sign) and sign == 'o'):
            msg.showinfo ("result","Player Two Wins !!")
            root.destroy()        
    
    if digit==4 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark = 'x'
            panels[digit] = mark
        elif count%2!=0:
            mark = 'o'
            panels[digit] = mark
        btn4.config(text= mark)
        count = count+1
        sign=mark
        if (win(panels,sign) and sign == 'x'):
            msg.showinfo ("result","Player One Wins !!")
            root.destroy()
        elif (win(panels,sign) and sign == 'o'):
            msg.showinfo ("result","Player Two Wins !!")
            root.destroy()
    
    if digit==5 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark = 'x'
            panels[digit] = mark
        elif count%2!=0:
            mark = 'o'
            panels[digit] = mark
        btn5.config(text= mark)
        count = count+1
        sign=mark
        if (win(panels,sign) and sign == 'x'):
            msg.showinfo ("result","Player One Wins !!")
            root.destroy()
        elif (win(panels,sign) and sign == 'o'):
            msg.showinfo ("result","Player Two Wins !!")
            root.destroy()

    if digit==6 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark = 'x'
            panels[digit] = mark
        elif count%2!=0:
            mark = 'o'
            panels[digit] = mark
        btn6.config(text= mark)
        count = count+1
        sign=mark
        if (win(panels,sign) and sign == 'x'):
            msg.showinfo ("result","Player One Wins !!")
            root.destroy()
        elif (win(panels,sign) and sign == 'o'):
            msg.showinfo ("result","Player Two Wins !!")
            root.destroy()   

    if digit==7 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark = 'x'
            panels[digit] = mark
        elif count%2!=0:
            mark = 'o'
            panels[digit] = mark
        btn7.config(text= mark)
        count = count+1
        sign=mark
        if (win(panels,sign) and sign == 'x'):
            msg.showinfo ("result","Player One Wins !!")
            root.destroy()
        elif (win(panels,sign) and sign == 'o'):
            msg.showinfo ("result","Player Two Wins !!")
            root.destroy() 

    if digit==8 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark = 'x'
            panels[digit] = mark
        elif count%2!=0:
            mark = 'o'
            panels[digit] = mark
        btn8.config(text= mark)
        count = count+1
        sign=mark
        if (win(panels,sign) and sign == 'x'):
            msg.showinfo ("result","Player One Wins !!")
            root.destroy()
        elif (win(panels,sign) and sign == 'o'):
            msg.showinfo ("result","Player Two Wins !!")
            root.destroy()  

    if digit==9 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark = 'x'
            panels[digit] = mark
        elif count%2!=0:
            mark = 'o'
            panels[digit] = mark
        btn9.config(text= mark)
        count = count+1
        sign=mark
        if (win(panels,sign) and sign == 'x'):
            msg.showinfo ("result","Player One Wins !!")
            root.destroy()
        elif (win(panels,sign) and sign == 'o'):
            msg.showinfo ("result","Player Two Wins !!")
            root.destroy()
       

btn1 = Button(root,width=15,height=7,font=('Times 16 bold'),command = lambda:checker(1))
btn1.grid(row=1,column=1)

btn2 = Button(root,width=15,height=7,font=('Times 16 bold'),command = lambda:checker(2))
btn2.grid(row=1,column=2)

btn3 = Button(root,width=15,height=7,font=('Times 16 bold'),command = lambda:checker(3))
btn3.grid(row=1,column=3)

btn4 = Button(root,width=15,height=7,font=('Times 16 bold'),command = lambda:checker(4))
btn4.grid(row=2,column=1)

btn5 = Button(root,width=15,height=7,font=('Times 16 bold'),command = lambda:checker(5))
btn5.grid(row=2,column=2)

btn6 = Button(root,width=15,height=7,font=('Times 16 bold'),command = lambda:checker(6))
btn6.grid(row=2,column=3)

btn7 = Button(root,width=15,height=7,font=('Times 16 bold'),command = lambda:checker(7))
btn7.grid(row=3,column=1)

btn8 = Button(root,width=15,height=7,font=('Times 16 bold'),command = lambda:checker(8))
btn8.grid(row=3,column=2)

btn9 = Button(root,width=15,height=7,font=('Times 16 bold'),command = lambda:checker(9))
btn9.grid(row=3,column=3)



root.mainloop()