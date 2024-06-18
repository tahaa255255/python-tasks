import pyautogui
import pyscreeze

def install(ex_name,ex_icon):
    counter=0
    location=None
    while location==None:
        counter+=1
        if counter==5:
            counter=0
            break
        try :
            if counter==1:
                location=pyautogui.locateOnScreen("extension icon1.png")
                pyautogui.moveTo(location)
                break
            elif counter==2:
                location=pyautogui.locateOnScreen("extension icon2.png")
                pyautogui.moveTo(location)
        except:
            print("image not found will try again !")  
            pyautogui.sleep(1) 
            

    pyautogui.leftClick()
    pyautogui.sleep(1)
    counter=0
    location=None
    while location==None:
        counter+=1
        if counter ==5:
            counter=0
            break
        try :
            if counter==1:
                location=pyautogui.locateOnScreen("clear bar icon.png")
                pyautogui.moveTo(location)
                counter=0
                break
            elif counter==2:
                location=pyautogui.locateOnScreen("clear bar icon2.png")
                pyautogui.moveTo(location)
                break
        except:
            print("image not found will try again !")
            pyautogui.sleep(1)   

    pyautogui.leftClick()
    pyautogui.sleep(2)
    location=None
    while location==None:
        counter+=1
        if counter ==5:
            counter=0
            break
        try :
            location=pyautogui.locateOnScreen("search bar icon.png")
            pyautogui.moveTo(location)
        except:
            print("image not found will try again !")
            pyautogui.sleep(1)   

    pyautogui.leftClick()
    pyautogui.write(ex_name)
    pyautogui.sleep(7)
    counter=0
    location=None
    while location==None:
        counter+=1
        if counter ==5:
            break
        try :
            location=pyautogui.locateOnScreen(ex_icon)
            pyautogui.moveTo(location)
        except:
            print("image not found will try again !")
            pyautogui.sleep(1)   
        
    pyautogui.leftClick()
    counter=0
    pyautogui.sleep(2)
    location=None
    while location==None:
        counter+=1
        if counter ==5:
            break
        try :
            location=pyautogui.locateOnScreen("uninstall icon.png")
            pyautogui.confirm("the "+ex_name+" is already installed")
        except:
            location=pyautogui.locateOnScreen("install icon.png")
            pyautogui.moveTo(location)
    pyautogui.leftClick()
    pyautogui.sleep(2)
    counter=0
    location=None
    while location==None:
        counter+=1
        if counter==5:
            counter=0
            break
        try :
            if counter==1:
                location=pyautogui.locateOnScreen("extension icon1.png")
                pyautogui.moveTo(location)
                break
            elif counter==2:
                location=pyautogui.locateOnScreen("extension icon2.png")
                pyautogui.moveTo(location)
        except:
            print("image not found will try again !")   
            

    pyautogui.leftClick()
    pyautogui.sleep(1)
#start vs code
pyautogui.hotkey("win",'r')
pyautogui.sleep(1)
pyautogui.press("backspace")
pyautogui.write("code")
pyautogui.sleep(1)
pyautogui.hotkey("ctrl","shift","enter")
location=None
while location==None:
    try:
        location=pyautogui.locateOnScreen("vscode icon.png")
        pyautogui.moveTo(location)
    except:
        pyautogui.sleep(2)    

pyautogui.leftClick()
################################################################################
#install clangd mate
################################################################################
install("clangd","clangd icon.png")
################################################################################
#install c++ test mate
################################################################################
install("c++ testmate","c++ testmate icon.png")
################################################################################
#install c++ helper
################################################################################
install("c++ helper","c++ helper icon.png")
################################################################################
#install cmake
################################################################################
install("cmake","cmake icon.png")
################################################################################
#install c++ helper
################################################################################
install("cmake tools","cmake tools icon.png")
