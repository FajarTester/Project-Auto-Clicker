import ctypes
import time
import threading
import keyboard

delay = 0.01
min_delay = 0.0005
max_delay = 1.0
step = 0.001

running = False
click_pos = None
thread = None
area = None  # (x1, y1, x2, y2)

def click_left(x=None, y=None):
    if x is not None and y is not None:
        ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)

def get_mouse_position():
    cursor = ctypes.wintypes.POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor))
    return cursor.x, cursor.y

def autoclicker():
    global running
    while running:
        x, y = get_mouse_position()

        # 🔒 Cek apakah mouse di dalam area yang diizinkan
        if area:
            x1, y1, x2, y2 = area
            if not (x1 <= x <= x2 and y1 <= y <= y2):
                time.sleep(0.05)
                continue

        if click_pos:
            click_left(*click_pos)
        else:
            click_left()
        time.sleep(delay)

def start_clicker():
    global running, thread
    if not running:
        running = True
        thread = threading.Thread(target=autoclicker)
        thread.start()
        print(f"✅ Auto-clicker aktif ({1/delay:.0f} CPS)")

def stop_clicker():
    global running
    running = False
    print("🛑 Auto-clicker berhenti.")

def increase_speed():
    global delay
    delay = max(min_delay, delay - step)
    print(f"⚡ Lebih cepat ({1/delay:.0f} CPS)")

def decrease_speed():
    global delay
    delay = min(max_delay, delay + step)
    print(f"🐢 Lebih lambat ({1/delay:.0f} CPS)")

def set_area():
    global area
    print("👉 Arahkan kursor ke pojok kiri atas area dan tekan ENTER")
    keyboard.wait("enter")
    x1, y1 = get_mouse_position()

    print("👉 Arahkan kursor ke pojok kanan bawah area dan tekan ENTER")
    keyboard.wait("enter")
    x2, y2 = get_mouse_position()

    area = (x1, y1, x2, y2)
    print(f"📏 Area dibatasi ke: {area}")

def clear_area():
    global area
    area = None
    print("🌍 Batas area dihapus, klik di seluruh layar diizinkan.")

# ==== HOTKEYS ====
keyboard.add_hotkey("f5", start_clicker)
keyboard.add_hotkey("f6", stop_clicker)
keyboard.add_hotkey("f9", increase_speed)
keyboard.add_hotkey("f10", decrease_speed)
keyboard.add_hotkey("f11", set_area)
keyboard.add_hotkey("f12", clear_area)

print("""
🎯 AUTO CLICKER DENGAN AREA BATAS
=================================
F5  → Mulai auto-click
F6  → Berhenti
F9  → Tambah kecepatan
F10 → Kurangi kecepatan
F11 → Set area klik (klik hanya di dalam area ini)
F12 → Hapus batas area
ESC → Keluar
=================================
""")

keyboard.wait("esc")
