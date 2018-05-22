import win32com.client as wincl
import webbrowser
import pyautogui as pag

#Imported shortcuts

PasswordList = {}
MessageList = {}
InputPasswordMessageList = {}
WrongPasswordMessageList = {}
RightPasswordMessageList = {}
PasswordList[0] = 'admin'
InputPasswordMessageList[0] = 'Please input password'
WrongPasswordMessageList[0] = 'Incorrent Password!'
RightPasswordMessageList[0] = 'Correct Password!'

#Reset Variables 

#Makes the computer talk
def Talk(words):
        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak(words)
        return 202

#Opens website in default browser
def OpenWebsite(website):
        webbrowser.open(website)
        return 202

#Sets password to input ID in list
def SetPassword(Password, Id=1):
        PasswordList[Id] = Password
        return 202

#Deletes the password with input ID by replacing it with an empty string
def DeletePassword(Id):
        PasswordList[Id] = ''
        return 202
      
#Allows to customize password input screen. Should use with an if statement to test if wrong or right
def AskPassword(Id, InputMessageID = 0, WrongMessageID = 0, RightMessageID = 0):
        TempWrongMessage = WrongPasswordMessageList[WrongMessageID]
        TempInputMessage = InputPasswordMessageList[InputMessageID]
        TempRightMessage = RightPasswordMessageList[RightMessageID]
        InputPassword = input(TempInputMessage + ": ")
        if(InputPassword == PasswordList[Id]):
                print TempRightMessage
                return True
        else:
                print TempWrongMessage
                return False
                
def SetPasswordMessage(message, type, id = 1):
        if(len(message) > 0):
                if(len(type) > 0):
                        if(type == 'Input'):
                                InputPasswordMessageList[id] = message
                        elif(type == 'Wrong'):
                                WrongPasswordMessageList[id] = message
                        elif (type == 'Right'):
                                RightPasswordMessageList[id] = message
                        else:
                                print "There was an error! It seems you did not input the correct Password Message Type! The valid types are 'Input', 'Wrong', 'Right'. Please use one of these."
                else:
                        print "There was an error! Or you did not enter a message!"
        else:
                print "There was an error! Or you did not enter a message!"

#Allows to customize password input screen. Should use with an if statement to test if wrong or right
def AskPasswordGUI(Id, InputMessageID = 0, WrongMessageID = 0, RightMessageID = 0):
        TempWrongMessage = WrongPasswordMessageList[WrongMessageID]
        TempInputMessage = InputPasswordMessageList[InputMessageID]
        TempRightMessage = RightPasswordMessageList[RightMessageID]
        InputPassword = pag.password(text=TempInputMessage + " :", title='Input Password', )
        if(InputPassword == PasswordList[Id]):
                print TempRightMessage
                return True
        else:
                print TempWrongMessage
                return False

def 