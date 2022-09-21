""" Even driven Programming """

""" A Brieft Studyin in Handling Life Events"""

import tkinter 

# handler for timer event
def alam():
     print('Calling the Pizza Company.')

# handler for rining doorbell
def doorbell():
    print('Ding Dong!')
    print('Opening the Door')

# handler for when the phone rings
def phonecall():
    print('Ansering the phone')

# create buttons and assing callbacks
root = tkinter.Tk()
tkinter.Button(root, text='Ring Doorbell', command=doorbell).pack()
tkinter.Button(root, text='Call Phone', command=phonecall).pack()
               

# set a timer for 1 second
root.after(4000, alarm)

# start the even loop
root.mainloop()
                                                
