import keyboard
import pyperclip
import pyautogui
import time



proposalTitle = []
proposalContent = []

printType = 0 
printIndex = 0

def setProposalData():
    proposalCnt = 0
    global proposalTitle
    global proposalContent
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
                
                
                
def on_ctrl_shit_v():
    global printType
    global printIndex
    
    print("Ctrl + F1 detected")

    # Change clipboard content
    new_text = ''
    
    if printType==0:
        new_text = proposalTitle[printIndex % (len(proposalTitle))]
        printType = 1
    else:
        new_text = proposalContent[printIndex % (len(proposalTitle))]
        printType = 0
        
    pyperclip.copy(new_text)
    print("Clipboard updated")

    # Small delay before paste to ensure the clipboard is ready
    time.sleep(0.1)

    # Simulate Ctrl + V (paste)
    pyautogui.hotkey('ctrl', 'v')
    print("Simulated Ctrl + V")
    printIndex+=1
    keyboard.send('tab')

setProposalData()
# Register the hotkey
keyboard.add_hotkey('ctrl+up', on_ctrl_shit_v)

print("Press Ctrl + E to trigger action. Press ESC to quit.")
keyboard.wait('esc')
