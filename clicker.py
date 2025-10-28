import pyautogui
import keyboard
import time
import threading

clicking = False
delay = 0.01  default 100 CPS
click_count = 0

def clicker():
    global clicking, delay, click_count
    while True:
        if clicking:
            pyautogui.click()
            click_count += 1
            time.sleep(delay)
        else:
            time.sleep(0.1)

def cps_monitor():
    global click_count
    while True:
        if clicking:
            current = click_count
            time.sleep(1)
            cps = click_count - current
            print(f"[CPS] {cps} clicks/sec (delay={delay:.4f}s)")
        else:
            time.sleep(1)

def toggle_clicking():
    global clicking, click_count
    clicking = not clicking
    click_count = 0
    print(f"[INFO] Auto-clicker {'ON' if clicking else 'OFF'}")

def increase_speed():
    global delay
    delay = max(0.0005, delay - 0.001)
    print(f"[INFO] Speed up → Delay: {delay:.4f}s (~{1/delay:.0f} CPS)")

def decrease_speed():
    global delay
    delay += 0.001
    print(f"[INFO] Slow down → Delay: {delay:.4f}s (~{1/delay:.0f} CPS)")

def main():
    print("===== Auto Clicker with CPS Monitor =====")
    print("[F6] Start/Stop clicking")
    print("[F8] Increase speed")
    print("[F9] Decrease speed")
    print("[ESC] Exit program\n")

    threading.Thread(target=clicker, daemon=True).start()
    threading.Thread(target=cps_monitor, daemon=True).start()

    while True:
        if keyboard.is_pressed("f6"):
            toggle_clicking()
            time.sleep(0.3)
        elif keyboard.is_pressed("f8"):
            increase_speed()
            time.sleep(0.2)
        elif keyboard.is_pressed("f9"):
            decrease_speed()
            time.sleep(0.2)
        elif keyboard.is_pressed("esc"):
            print("Exiting...")
            break
        time.sleep(0.01)

if __name__ == "__main__":
    main()
