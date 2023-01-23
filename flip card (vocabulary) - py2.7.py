from Tkinter import *
import tkFileDialog, os, random


class Voca:

    def extract(self):

        Name = tkFileDialog.askopenfilename(initialdir='C:\Users\Won\OneDrive\Document\Vocab Flip Card', \
            title='pick a file', filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        self.AA = open(Name, 'r')
        print (Name)
        RR = self.AA.readlines()
        self.AA.close()
        RR.append('@')
        self.Keys = []

        for i in RR:
            if i[0] == '@':
                if self.count != 0:
                    self.dic[aa] = cc

                self.count += 1
                cc = []
                aa = i[1:len(i) - 1]
                self.Keys.append(aa)

            elif i[0] == '=':
                bb = '\n' + i[0:]
                cc.append(bb)

        self.Keys = self.Keys[:len(self.Keys) - 1]  # the x number of the elements in the list will be saved
        self.display()

    def display(self):
        self.Word_Label['text'] = (self.Keys[self.WordNum])
        self.Example_Note.delete('1.0', END)
        for Example in self.dic[self.Keys[self.WordNum]]:
            self.Example_Note.insert(END, Example)
        # self.Example_Note.update()
        self.File_Name['text'] = os.path.basename(self.AA.name)
        self.CardNum['text'] = ('{} / {}'.format(self.WordNum + 1, len(self.Keys)))

    def previous(self):
        self.WordNum -= 1
        if self.WordNum < 0: self.WordNum = len(self.Keys) - 1  # number counts from "0" not "1"
        # print self.WordNum
        self.display()

    def next(self):
        self.WordNum += 1
        if self.WordNum > len(self.Keys) - 1: self.WordNum = 0  # number counts from "0" not "1"
        # print self.WordNum
        self.display()

    def shuffle(self):
        random.shuffle(self.Keys)
        self.WordNum = 0
        self.display()

    def KeyControl(self, event):
        if event.keysym == "Left":
            self.previous()
        elif event.keysym == "Right":
            self.next()
        elif event.keysym == "o":
            self.extract()
        elif event.keysym == "s":
            self.shuffle()
        elif event.keysym == "Escape":
            self.win.destroy()
        elif event.keysym == "space":
            self.next()
        elif event.keysym == "q":
            self.win.destroy()

    def __init__(self):

        self.dic = {}
        self.count = 0
        self.WordNum = 0

        self.win = Tk()
        self.win.title('Flip Card')

        fr1 = Frame(self.win)
        fr2 = Frame(self.win)
        fr3 = Frame(self.win)
        fr4 = Frame(self.win)

        fr1.grid(row=0, column=0)
        fr2.grid(row=1, column=0)
        fr3.grid(row=2, column=0)
        fr4.grid(row=3, column=0)

        self.Word_Label = Label(fr1, text='Choose a Deck', width=15, height=2, font='arial 18 bold')
        self.Word_Label.pack()

        self.Example_Note = Text(fr2, width=100, height=15, bg='light grey', font='arial 15')
        self.Example_Note.pack()

        self.Open_Bt = Button(fr3, text='Open', command=self.extract, font='arial 12')
        self.Previous_Bt = Button(fr3, text='Previous Word', command=self.previous, font='arial 12')
        self.Next_Bt = Button(fr3, text='Next Word', command=self.next, font='arial 12')
        self.Shuffle_Bt = Button(fr3, text='Shuffle', command=self.shuffle, font='arial 12')

        self.Open_Bt.grid(row=0, column=0, padx=5)
        self.Previous_Bt.grid(row=0, column=1, padx=5)
        self.Next_Bt.grid(row=0, column=2, padx=5)
        self.Shuffle_Bt.grid(row=0, column=3, padx=5)

        self.File_Name = Label(fr4, text='Choose a Deck', font='arial 10')
        self.CardNum = Label(fr4, text='? / ?', font='arial 10')
        self.File_Name.grid(row=0, column=0, padx=10)
        self.CardNum.grid(row=0, column=1, padx=10)

        self.win.bind('<Key>', self.KeyControl)

        self.win.mainloop()


if __name__ == '__main__':
    Voca()
