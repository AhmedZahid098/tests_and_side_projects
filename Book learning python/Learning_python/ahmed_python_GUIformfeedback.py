from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Feedback:
    '''This is a form for fun'''

    def __init__(self, master):
        master.title('Feedback')
        master.resizable(False, False)
        master.config(background='grey')

        # styling
        self.style = ttk.Style()
        self.style.configure('TFrame', background='grey')
        self.style.configure('TLabel', background='grey')
        self.style.configure('TEntry', background='grey',
                             font=('arial', 10, 'bold'))
        self.style.configure('TButton', background='grey',
                             font=('arial', 10))

        # header frame
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        # image
        self.logo = PhotoImage(file='D:\python_logo.gif').subsample(3, 3)
        self.label_image = ttk.Label(self.frame_header, image=self.logo)
        self.label_image.grid(row=0, column=0, rowspan=2, padx=5, pady=5)
        # header
        self.label_header = ttk.Label(
            self.frame_header, text='Thank You!', font=('arial', 20, 'bold'))
        self.label_header.grid(row=0, column=1, padx=5, pady=5)
        # message
        self.label_message = ttk.Label(
            self.frame_header, text='Hope you are enjoying your life.'
            + ' Here is small feedback to make things wonderful between us.',
            wraplength=400, font=('arial', 10))  # message
        self.label_message.grid(row=1, column=1, padx=5, pady=5)

        # content
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()
        # name
        self.label_name = ttk.Label(
            self.frame_content, text=' Name:', font=('arial', 10))
        self.label_name.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        # email
        self.label_email = ttk.Label(
            self.frame_content, text=' Email:', font=('arial', 10))
        self.label_email.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        # comments
        self.label_comment = ttk.Label(
            self.frame_content, text='Comments:', font=('arial', 10))
        self.label_comment.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        # stringVARs
        self.name_text = StringVar()
        self.email_text = StringVar()
        self.comment_text = StringVar()
        # entries
        self.entry_name = ttk.Entry(
            self.frame_content, width=30, textvariable=self.name_text)
        self.entry_name.grid(row=1, column=0, padx=5)
        self.entry_email = ttk.Entry(
            self.frame_content, width=30, textvariable=self.email_text)
        self.entry_email.grid(row=1, column=1, padx=5)
        self.entry_comment = Text(self.frame_content, width=50, height=10,
                                  wrap='word')
        self.entry_comment.grid(row=3, column=0, columnspan=2)
        # scrollbar
        self.text_scrollbar = ttk.Scrollbar(self.frame_content,
                                            orient=VERTICAL, command=self.entry_comment.yview)
        self.entry_comment.config(
            yscrollcommand=self.text_scrollbar.set)
        self.text_scrollbar.grid(
            row=3, column=1, columnspan=2, sticky='e' + 'ns')
        # buttons
        self.button1 = ttk.Button(
            self.frame_content, text='Submit', command=self.submit)
        self.button1.grid(row=4, column=0, padx=5, pady=5)
        self.button2 = ttk.Button(
            self.frame_content, text='Clear', command=self.clear)
        self.button2.grid(row=4, column=1, padx=5)

        # Methods
    def submit(self):
        if len(str(self.name_text.get())) == 0 and len(str(self.email_text.get())) == 0 and len(str(self.entry_comment.get(1.0, END))) == 1:
            self.message_error = messagebox.showerror(
                title='Error', message='Need to fill all the feilds')
        else:
            print(f'Name: {self.name_text.get()}')
            print(f'Email: {self.email_text.get()}')
            print(f'Comment: {self.entry_comment.get(1.0, END)}')
            self.clear()
            self.message = messagebox.showinfo(
                title='Feedback', message='Thank you for your precious time')

    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.entry_comment.delete(1.0, 'end')


def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()


if __name__ == '__main__':
    main()
