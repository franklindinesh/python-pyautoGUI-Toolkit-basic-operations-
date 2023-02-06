import pyautogui  # import the revelant modules
import time

# give the python file some times before continuing
time.sleep(3)

# mouse functions:
print(pyautogui.size())   # prints the resolutions of your screen

# print the current position of the mouse
#print(pyautogui.position()) # it going left side

# moves the mouse over time(3 seconds)
#pyautogui.moveTo(200, 150, 3)
#                 x    y  sec


# move the mouse relative to its current position
#pyautogui.moveRel(100,100,3)

# click
#pyautogui.click(400,400,3,3,button="right")  #500-X axis , 500-Y axis , 3 - number of click , 3-duration time limit
#pyautogui.tripleClick()
#pyautogui.doubleClick()
#pyautogui.leftClick()
#pyautogui.rightClick()


'''
# scroll up
pyautogui.scroll(3000)

# scroll down
pyautogui.scroll(-5000)

pyautogui.scroll(3000)
pyautogui.scroll(-5000)
'''

'''
# mouse up and down
pyautogui.mouseUp(100,100,button="left")
pyautogui.mouseDown(100,100,button="left")
'''

'''
# example of mouse up and down
pyautogui.mouseDown(300, 400, button="left")
pyautogui.moveTo(800, 400, 3)
pyautogui.mouseUp()
pyautogui.moveTo(1000, 400, 3)
'''


# spiral drawing using pyautogui
time.sleep(1)
distance = 300
while distance > 0:
    pyautogui.dragRel(distance, 0, 1, button="left")  # X-axis
    distance = distance - 20

    pyautogui.dragRel(0, distance, 1, button="left")  # Y-axis
    pyautogui.dragRel(-distance, 0, 1, button="left")
    distance = distance - 20

    pyautogui.dragRel(0, -distance, 1, button="left")  # x -axix -leftside
time.sleep(2)



# Instagram,youtube Auto play,pause click
time.sleep(2)
#range will be the number of tiktok's you want to like
for i in range(4):
    #pyautogui.moveTo(450,500)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    #pyautogui.moveTo(854,515)
    time.sleep(1)
    pyautogui.leftClick()
