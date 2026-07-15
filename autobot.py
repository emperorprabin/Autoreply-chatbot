import pyautogui
import pyperclip
import time
import os
from google import genai
from openai import OpenAI
import re
 
def is_last_message_from_sender(chat_history, name="Aishu Di"):
    pattern = re.compile(r'^\[.*?\]\s*(.*?):\s*(.*)$')
    last_sender = None
    for raw_line in chat_history.strip().splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if not line.startswith('['):
            continue
        match = pattern.match(line)
        if match:
            last_sender = match.group(1).strip()
 
    if last_sender is None:
        return False
 
    return last_sender.lower() == name.lower()


icon_x, icon_y = 950, 1168
pyautogui.click(icon_x, icon_y)
time.sleep(1)  
while True:
    start_x, start_y = 896,239
    end_x, end_y = 1850, 1050

    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y, duration=0.5) 
    pyautogui.mouseUp()
    time.sleep(0.3)

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.3)
    pyautogui.click(1370,538)

    chat_history = pyperclip.paste()

    print("Chat History:")
    print(chat_history)

    if is_last_message_from_sender(chat_history) is True:
        client = OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama"  # required by the library, but ignored locally
        )

        response = client.chat.completions.create(
            model="mistral",
            messages=[
                {"role": "system", "content": "You are a auto chatbot responding as a human that can speak both english and nepali. you analyze chat history and respond like prabin from nepal.Output should be the next chat as prabin.Give me short answers."},
                {"role": "user", "content": chat_history}
            ]
        )

        print(response.choices[0].message.content)
        pyperclip.copy(response.choices[0].message.content)

        input_x, input_y = 1020, 1069
        pyautogui.click(input_x, input_y)
        time.sleep(0.5) 

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.3)

        pyautogui.press('enter')
    
    """else:
        break"""