import keyboard
import tkinter as tk
import pyperclip
import time
import pyautogui
import random

emailName = []
emailAddress = []
emailCnt = 0
proposalTitle = []
proposalContent = []
proposalCnt = 0
curEmailIndex = 0
curProposalIndex = random.randint(0,6)


def setEmailAddress():
    global emailCnt
    global emailName
    global emailAddress  # So we update the global list, not a local one
    with open("mailaccount.txt", "r" , encoding="utf-8") as file:
        content = file.read()
        tmp = content.split('\n')
        for subtmp in tmp:
            subArr = subtmp.strip().split('\t')
            if len(subArr) == 2:
                title = subArr[0].strip()
                body = subArr[1].strip()
                emailName.insert(emailCnt, title)
                emailAddress.insert(emailCnt, body)
                emailCnt+=1

def setProposalData():
    global proposalData  # So we update the global list, not a local one
    global proposalCnt
    with open("proposal.txt", "r" ,encoding="utf-8") as file:
        content = file.read()
        proposals = content.split('-------------------------------------------------')
        
        for proposal in proposals:
            parts = proposal.strip().split('************************************************')
            if len(parts) == 2:
                title = parts[0].strip()
                body = parts[1].strip()
                proposalTitle.insert(proposalCnt, title)
                proposalContent.insert(proposalCnt, body)
                proposalCnt += 1
                
                
def on_ctrl_f11():
    global emailAddress 
    global proposalTitle 
    global proposalContent 
    global proposalCnt 
    global curEmailIndex 
    global curProposalIndex 
    
    print("Ctrl + F11 was pressed & Start with Text Past")
    cntIndex = 0
    while curEmailIndex < len(emailAddress) :
        print(f"{curEmailIndex}-{emailAddress[curEmailIndex]}")
        if (cntIndex % 8 == 0 ):
            time.sleep(1)
            keyboard.press('ctrl')
            keyboard.press('windows')
            keyboard.press('left')  
            keyboard.release('ctrl')
            keyboard.release('windows')
            keyboard.release('left')
            time.sleep(0.5)
        if (cntIndex % 48 == 0 and cntIndex > 0):
            for i in range(1,6):
                time.sleep(1)
                keyboard.press('ctrl')
                keyboard.press('windows')
                keyboard.press('right')  
                keyboard.release('ctrl')
                keyboard.release('windows')
                keyboard.release('right')
                time.sleep(1)
        
        xpos=100
        ypos=100
        if cntIndex % 8 == 0 : 
            xpos=-2481
            ypos=6
        if cntIndex % 8 == 1 : 
            xpos=-2477
            ypos=515
        if cntIndex % 8 == 2 : 
            xpos=-1621
            ypos=4
        if cntIndex % 8 == 3 : 
            xpos=-1616
            ypos=513
        if cntIndex % 8 == 4 : 
            xpos=89
            ypos=167
        if cntIndex % 8 == 5 : 
            xpos=98
            ypos=862
        if cntIndex % 8 == 6 : 
            xpos=1369
            ypos=170
        if cntIndex % 8 == 7 : 
            xpos=1371
            ypos=864
            
        pyautogui.moveTo(xpos, ypos, duration=0.2)
        pyautogui.click()
        time.sleep(1)
        # Set clipboard text with 
        # time.sleep(2)
        pyperclip.copy(emailAddress[curEmailIndex])
        keyboard.press('ctrl')
        keyboard.press('v')
        keyboard.release('v')
        keyboard.release('ctrl')
        
        time.sleep(1)
        tmp = curProposalIndex%len(proposalContent)
        keyboard.send('tab')
        pyperclip.copy(f"Hi {emailName[curEmailIndex]}, {proposalTitle[tmp]}")        
        keyboard.press('ctrl')
        keyboard.press('v')
        keyboard.release('v')
        keyboard.release('ctrl')
        
        time.sleep(1)
        
        keyboard.send('tab')
        pyperclip.copy(proposalContent[tmp])        
        keyboard.press('ctrl')
        keyboard.press('v')
        keyboard.release('v')
        keyboard.release('ctrl')
        
        time.sleep(1)
        keyboard.press('ctrl')
        keyboard.press('enter')
        keyboard.release('enter')
        keyboard.release('ctrl')
        time.sleep(0.5)
        
        curEmailIndex+=1
        curProposalIndex+=1
        cntIndex+=1
    
    print("Ended")

root = tk.Tk()
root.bind('<Control-F11>', on_ctrl_f11)


keyboard.add_hotkey('ctrl+f11', on_ctrl_f11)

def main():
    setEmailAddress()
    setProposalData()
    print("Press Ctrl+F11...")
    keyboard.wait('esc')  # Wait until Esc is pressed to exit

main()