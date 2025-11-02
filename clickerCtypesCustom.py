import ctypes
import time
import threading
import keyboard  


delay = 0.01        #! default: 10ms per klik (≈100 CPS)
min_delay = 0.0005  #! tercepat
max_delay = 1.0     #! terlambat
step = 0.001        #! langkah perubahan tiap F9/F10

running = False
target_mode = False
click_pos = None
thread = None

#! ==== FUNGSI DASAR ====
def click_left(x=None, y=None):
    if x is not None and y is not None:
        ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # LEFTDOWN
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # LEFTUP

def get_mouse_position():
    cursor = ctypes.wintypes.POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor))
    return cursor.x, cursor.y

def autoclicker():
    global running
    while running:
        if click_pos:
            click_left(*click_pos)
        else:
            click_left()
        time.sleep(delay)

#! ==== KONTROL ====
def start_clicker():
    global running, thread
    if not running:
        running = True
        thread = threading.Thread(target=autoclicker)
        thread.start()
        if click_pos:
            print(f"🔥 Auto-clicker aktif di posisi {click_pos} ({1/delay:.0f} CPS)")
        else:
            print(f"🔥 Auto-clicker aktif di posisi mouse ({1/delay:.0f} CPS)")

def stop_clicker():
    global running
    running = False
    print("🛑 Auto-clicker berhenti.")

def change_speed():
    global delay, running
    was_running = running
    if running:
        stop_clicker()

    try:
        new_delay = float(input("Masukkan delay baru (contoh: 0.01 = 100 CPS): "))
        if new_delay < min_delay:
            new_delay = min_delay
        elif new_delay > max_delay:
            new_delay = max_delay
        delay = new_delay
        print(f"✅ Kecepatan diubah ke {1/delay:.0f} CPS")
    except ValueError:
        print("❌ Input tidak valid.")

    if was_running:
        start_clicker()

def increase_speed():
    global delay
    delay = max(min_delay, delay - step)
    print(f"⚡ Lebih cepat! Sekarang {1/delay:.0f} CPS")

def decrease_speed():
    global delay
    delay = min(max_delay, delay + step)
    print(f"🐢 Lebih lambat! Sekarang {1/delay:.0f} CPS")

def set_target():
    global click_pos
    click_pos = get_mouse_position()
    print(f"🎯 Target dikunci di {click_pos}")

def clear_target():
    global click_pos
    click_pos = None
    print("🌀 Target dilepas, klik mengikuti posisi mouse.")

#? ==== HOTKEYS ====
keyboard.add_hotkey("f5", set_target)
keyboard.add_hotkey("f6", start_clicker)
keyboard.add_hotkey("f7", stop_clicker)
keyboard.add_hotkey("f8", change_speed)
keyboard.add_hotkey("f9", increase_speed)
keyboard.add_hotkey("f10", decrease_speed)
keyboard.add_hotkey("f4", clear_target)

print("""
🎯 AUTO CLICKER — Versi Lengkap
=================================
F4  → Lepas target (klik ikut mouse)
F5  → Set target (klik di titik mouse sekarang)
F6  → Mulai auto-click
F7  → Berhenti
F8  → Ubah kecepatan manual
F9  → Tambah kecepatan
F10 → Kurangi kecepatan
ESC → Keluar
=================================
""")

keyboard.wait("esc")
