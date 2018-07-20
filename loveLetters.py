#!/usr/bin/env python

import sys
import imaplib
import time
import getpass
import email
import datetime
import mailbox
import tkinter
from guizero import App, Text

EMAIL_ACCOUNT = "doesmichaelmessages@gmail.com"
PASSWORD = "" #password for email account above

class Mail():
    def __init__(self):
        return
    #called to refresh the display with new text. if there's not an unread message in the inbox, nothing changes.
    def update_label(self):
        body = self.checkMail()
        text.value = body
        text.after(1000, self.update_label)
    
    #logs in to the email acct and returns the body of any unread message
    def checkMail(self):
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        self.mail.login(EMAIL_ACCOUNT, PASSWORD)
        self.mail.select('inbox')
        self.result, self.unRead = self.mail.search(None, 'UNSEEN') #get unread emails

        for num in self.unRead[0].split():
            typ, data = self.mail.fetch(num, '(RFC822)')
            msg = email.message_from_bytes(data[0][1])
            #get the body of the message
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True)
                    return (body)
        #logout
        self.mail.close()

if __name__ == '__main__':
    #setting TKinter/guizero text and background colors
    bgcolor = 'springgreen4'
    txtcolor = 'skyblue2'
    
    #start up GUI
    app = App(bg = bgcolor)
    
    #start an instance of the Mail class
    emai = Mail()

    #Guizero command to add text to the app object
    text = Text(app, text="hey lovebug", font = "Avenir Next", size=60, color=txtcolor)
    
    #accessing TKinter methods on guizero object text. Text wrapping is broken, and I can't get it to work properly.
    text.tk.wrap='char'

    #update the placeholder text after 1000ms, and update it continuously with the update_label method
    text.after(1000, emai.update_label)

    #change bool to true for fullscreen
    app.tk.wm_attributes("-fullscreen", False)

    #show the app. this has to be last for looping to occur. 
    app.display()
