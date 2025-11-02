import ctypes
import time
import threading
import keyboard  


def click_left():
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # LEFTDOWN
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # LEFTUP

running = False

def autoclicker():
    global running
    while running:
        click_left()
        time.sleep(0.001)

def start_clicker():
    global running
    if not running:
        running = True
        threading.Thread(target=autoclicker).start()
        print("Auto-clicker aktif!")

def stop_clicker():
    global running
    running = False
    print("Auto-clicker berhenti.")

keyboard.add_hotkey("f6", start_clicker)
keyboard.add_hotkey("f7", stop_clicker)
keyboard.add_hotkey("esc", lambda: print("Exiting...") or exit())

print("Tekan F6 untuk mulai, F7 untuk stop.")
keyboard.wait("esc")

