from tkinter import*
import tkinter.messagebox
import random

root = tkinter.Tk()
root.title("PROJECT ASD")
root.configure(background='pink')
root.geometry("1000x500")


class Queue_ku(object):
    def __init__(self):
        self.task = []

    def clear_listbox(self):
        lb_tasks.delete(0, "end")

    def update_listbox(self):
        self.clear_listbox()
        for ts in self.task:
            lb_tasks.insert("end", ts)
                
    def rekap(self):
        show = self.task
        tkinter.messagebox.showwarning("This","pesanan kamu %s" %show)

    def search(self):
        tasks = txt_input.get()
        if tasks in self.task:
            message = "Result: %s" %tasks
            lbl_display["text"] = message
            txt_input.delete(0, "end")
        else  :
            message = "Menu yang dicari tidak ada"
            lbl_display["text"] = message
    def enqueue(self):
        tasks = txt_input.get()
        if tasks != "":
                self.task.append(tasks)
                self.update_listbox()
        else:
                tkinter.messagebox.showwarning("Warning", "You need to enter a task.")
        txt_input.delete(0, "end")

    def dequeue(self):
        self.task.sort()
        self.update_listbox()
        
    def remove_all(self):
        confirmed = tkinter.messagebox.askyesno("Please Confirm", "Do you really want to delete all?")
        if confirmed == True :
            self.task = []
            self.update_listbox()

    def remove_one(self):
        tasks = lb_tasks.get("active")
        confirmed = tkinter.messagebox.askyesno("Please Confirm", "Do you really want to delete this?")
        if confirmed == True :
            if tasks in self.task :
                self.task.remove(tasks)
            self.update_listbox()


QH = Queue_ku()

#lblInfo = Label(Tops, font=('arial',50, 'bold'), text ="Intellegence Resto", fg='Steel Blue', bd=10, anchor='w')
#lblInfo.grid(row=0,column=0)

lbl_display = tkinter.Label(root, text="")
lbl_display.grid(row=9,column=1)

txt_input = tkinter.Entry(root, width=40, bg="white")
txt_input.grid(row=1,column=1)

btn_add_task = tkinter.Button(root, text="    Masukan    ", bg="pink", bd=5, command = QH.enqueue)
btn_add_task.grid(row=1,column=4)

btn_del_one = tkinter.Button(root, text="     Urutkan     ", bg="pink", bd=5, command= QH.dequeue)
btn_del_one.grid(row=2,column=4)

btn_remove_one = tkinter.Button(root, text="      Hapus      ", bg="pink",bd=5, command= QH.remove_one)
btn_remove_one.grid(row=3,column=4)

btn_remove_all = tkinter.Button(root, text="Hapus Semua", bg="pink",bd=5, command= QH.remove_all)
btn_remove_all.grid(row=4,column=4)

btn_number_of_tasks = tkinter.Button(root, text="      Rekap      ", bg="pink",bd=5, command = QH.rekap)
btn_number_of_tasks.grid(row=5,column=4)

btn_search = tkinter.Button(root, text="         Cari        ", bg="pink",bd=5, command = QH.search)
btn_search.grid(row=6,column=4)

btn_exit = tkinter.Button(root, text="      Keluar        ", bg="pink",bd=5, command=exit)
btn_exit.grid(row=7,column=4)

lb_tasks = tkinter.Listbox(root,  width=70, height=20, bg="powder blue")
lb_tasks.grid(row=2,column=1, rowspan=7)

#=============================================Daftar Menu===================================================================
lbl0 = Label(font=('arial', 18,'bold'), text="----DAFTAR MENU---- ", bd=5, bg ="pink")
lbl0 .grid(row=0, column=10)
lbl1 = Label(font=('arial', 12,'bold'), text="Ayam Kremes  = Rp. 11.000", bd=5, bg ="pink")
lbl1 .grid(row=1, column=10)
lbl2 = Label(font=('arial', 12,'bold'), text="Ayam Geprek  = Rp. 10.000", bd=5,bg ="pink")
lbl2 .grid(row=2, column=10)
lbl3 = Label(font=('arial', 12,'bold'), text="Soto Ayam    = Rp. 7.000", bd=5,bg ="pink")
lbl3 .grid(row=3, column=10)
lbl4 = Label(font=('arial', 12,'bold'), text="Sop Matahari = Rp. 12.000", bd=5, bg ="pink")
lbl4 .grid(row=4, column=10)
lbl5 = Label(font=('arial', 12,'bold'), text="Opor Ayam    = Rp. 15.000", bd=5, bg ="pink")
lbl5 .grid(row=5, column=10)


#--------------------------------------------Daftar Menu kanan-------------------------------------------------------------
lbl6 = Label(font=('arial',12 ,'bold'), text="Es Jeruk   = Rp. 5.000", bd=5,bg ="pink")
lbl6 .grid(row=1, column=11)
lbl7 = Label(font=('arial', 12,'bold'), text="Sirup       = Rp. 2.000", bd=5,bg ="pink")
lbl7 .grid(row=2, column=11)
lbl8 = Label(font=('arial', 12,'bold'), text="Capucino = Rp. 9.000", bd=5,bg ="pink")
lbl8 .grid(row=3, column=11)
lbl9 = Label(font=('arial', 12,'bold'), text="Teh         = Rp. 3.000", bd=5,bg ="pink")
lbl9 .grid(row=4, column=11)
lbl10 = Label(font=('arial', 12,'bold'), text="Air Botol = Rp. 5.000", bd=5,bg ="pink")
lbl10.grid(row=5, column=11)

root.mainloop()
