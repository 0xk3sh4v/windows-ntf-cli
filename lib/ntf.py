import ctypes
import time
import sys

class NOTIFYICONDATA(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_uint),
                ("hWnd", ctypes.c_void_p),
                ("uID", ctypes.c_uint),
                ("uFlags", ctypes.c_uint),
                ("uCallbackMessage", ctypes.c_uint),
                ("hIcon", ctypes.c_void_p),
                ("szTip", ctypes.c_char * 128),
                ("dwState", ctypes.c_uint),
                ("dwStateMask", ctypes.c_uint),
                ("szInfo", ctypes.c_char * 256),
                ("uTimeoutOrVersion", ctypes.c_uint),
                ("szInfoTitle", ctypes.c_char * 64),
                ("dwInfoFlags", ctypes.c_uint),
                ("guidItem", ctypes.c_byte * 16),
                ("hBalloonIcon", ctypes.c_void_p)]

NIF_INFO = 0x00000010
NIIF_INFO = 0x00000001
NIM_ADD = 0x00000000
NIM_MODIFY = 0x00000001
NIM_DELETE = 0x00000002

def show_notification(title, msg, sleeptime):
    nid = NOTIFYICONDATA()
    nid.cbSize = ctypes.sizeof(NOTIFYICONDATA)
    nid.uFlags = NIF_INFO
    nid.szInfo = msg.encode('utf-8')
    nid.szInfoTitle = title.encode('utf-8')
    nid.dwInfoFlags = NIIF_INFO

    shell32 = ctypes.windll.shell32
    shell32.Shell_NotifyIconA(NIM_ADD, ctypes.byref(nid))
    shell32.Shell_NotifyIconA(NIM_MODIFY, ctypes.byref(nid))

    time.sleep(sleeptime)
    shell32.Shell_NotifyIconA(NIM_DELETE, ctypes.byref(nid))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <title> <message> <time>")
        sys.exit(1)
    
    title = sys.argv[1]
    message = sys.argv[2]
    sleeptime = float(sys.argv[3])
    if sleeptime > 8:
        print("The notification will be auto deleted in 8 seconds, engaging the thread for 10s")
    show_notification(title, message, sleeptime)