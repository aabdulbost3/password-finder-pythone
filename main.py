import random
import pyautogui
# import numpys as np

chars = "qwertyuioplkjhgfdsazxcvbnm1234567890"

allchar = list(chars)

pwd = pyautogui.password("Enter » password")
sample_pwd = ""

while(sample_pwd != pwd):
    sample_pwd = random.choices(allchar, k=len(pwd))

    print("<===" + str(sample_pwd) + "===>")

    if(sample_pwd == list(pwd)):
        print("The passwordis : " +"".join(sample_pwd))
        break
    