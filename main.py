import time
import pyperclip
import pyautogui

print(pyautogui.size())
print(pyautogui.position())

CHROME_POS = (61, 229)
CHROME_CLOSE_POS = (3789, 40)
CHROME_SEARCH_BAR_POS = (410, 107)

HTML_TAG_POS = (1138, 1435)
EDIT_HTML_POS = (1158, 484)

NUM_PAGES = 9
BASE_URL = "https://wellfound.com/startups/l/india/artificial-intelligence?page="

for page in range(1, NUM_PAGES+1):
    pyautogui.click(x=CHROME_POS[0], y=CHROME_POS[1], clicks=2)
    time.sleep(2)

    pyautogui.click(x=CHROME_SEARCH_BAR_POS[0], y=CHROME_SEARCH_BAR_POS[1], clicks=1)
    pyautogui.typewrite(f"{BASE_URL}{page}")
    pyautogui.press('enter')
    time.sleep(2)

    pyautogui.hotkey('ctrl', 'shift', 'c')
    time.sleep(3)
    pyautogui.click(x=HTML_TAG_POS[0], y=HTML_TAG_POS[1], clicks=1)
    time.sleep(3)
    pyautogui.click(x=HTML_TAG_POS[0], y=HTML_TAG_POS[1], clicks=1, button="right")
    time.sleep(3)
    pyautogui.click(x=EDIT_HTML_POS[0], y=EDIT_HTML_POS[1])
    time.sleep(3)

    pyautogui.hotkey('ctrl', 'a')
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'c')

    html = pyperclip.paste()
    with open(f"./scraped_pages/{page}.txt", "w", encoding="utf-8") as f:
       f.write(html)

    pyautogui.click(x=CHROME_CLOSE_POS[0], y=CHROME_CLOSE_POS[1], clicks=1)
