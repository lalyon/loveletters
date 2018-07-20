# loveletters

## Overview
This is a Python script that logs in to an email, looks for unread messages, and pushes the body of unread messages to the screen.

### Requirements: 
- Guizero
- TKinter
- Mailbox python library
- imaplib python library
- getpass python library
- an Internet Connection

This app was made for use with a Raspberry Pi Zero W and TFT screen. The Guizero library is relatively new but well documented, and allows for customization of the text, background, font, text size, etc. 

###  What's working:
- accessing email
- extracting email body
- updating the GUI with the message

### What's not working:
- text wrapping

### What's next:
- add interactivity to allow for color changes of the GUI with clicks or touches
- add scrolling text
- enable emoji support
- update the screen without logging in and out every few seconds 
