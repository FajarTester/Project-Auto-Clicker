import pyautogui
import keyboard
import time
import threading
print("Click F6 to start Clicking")
print("Click F7 to stop Clicking")
print("Click ESC to exit the program")

clicking = False
delay = 0.01 

def clicker():
    global clicking, delay
    while True:
        if clicking: 
            pyautogui.click()
            time.sleep(delay)
        else:
            time.sleep(0.1)
            
            
def toggle_clicking():
    global clicking 
    clicking = not clicking
    print(f"[INFO] Auto-Clicker {'ON' if clicking else 'OFF'}")
    
    
def increase_speed():
    global delay
    delay = max(0.0005, delay - 0.001)
    print(f"[INFO] Speed up → Delay: {delay:.4f}s ({1/delay:.0f} CPS)")
    
    
def decrease_speed():
    global delay
    delay = delay + 0.001
    print(f"[INFO] Slow down → Delay: {delay:.4f}s ({1/delay:.0f} CPS)")
    
def main():
    print("=== Auto Clicker Started ===")
    print("[F6] Start/Stop Clicking")
    print("[F8] Increase Speed")
    print("[F9] Decrease Speed")
    print("[ESC] Exit Program")
    
    threading.Thread(target=clicker, daemon=True).start()
    
    while True:
        if keyboard.is_pressed('F6'):
            toggle_clicking()
            time.sleep(0.3)
        elif keyboard.is_pressed('F8'):
            increase_speed()
            time.sleep(0.3)
        elif keyboard.is_pressed('F9'):
            decrease_speed()
            time.sleep(0.3)
        elif keyboard.is_pressed('esc'):
            print("Exiting...")
            break
        else:
            time.sleep(0.1)
            
if __name__ == '__main__':
    main()