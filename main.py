import tkinter as tk
from tkinter import messagebox
import winreg

def gfew(vvc):
    mmop = False
    if not vvc.isalpha():
        mmop = True
    if vvc[0] != vvc[3]:
        mmop = True
    if ord(vvc[0]) != ord(vvc[-1]) - 4:
        mmop = True
    if not vvc[1].islower():
        mmop = True
    if not vvc[2].isalnum():
        mmop = True
    if mmop:
        return 'Key check failed on the first segment'
    return None


def gfaw(vvc):
    kklop = vvc[6:11]
    mmop = False
    if not kklop.isnumeric():
        mmop = True
    if int(kklop) % 2 != 0:
        mmop = True
    if kklop[0] == '0':
        mmop = True
    if kklop[0] != kklop[-1]:
        mmop = True
    if ord(vvc[0]) != int(kklop[:2]):
        mmop = True
    if mmop:
        return 'Key check failed on the second segment'
    return None


def gfaf(vvc):
    kklop = vvc[12:]
    mmop = False
    if ord(kklop[0]) >> 2 != 20:
        mmop = True
    diff = ord(vvc[4]) & ord(vvc[5])
    if diff > 10:
        diff = diff % 10
    if kklop[1] != str(diff):
        mmop = True
    if not kklop[2:].isnumeric():
        mmop = True
    num = 0
    try:
        num = int(kklop[2:])
    except ValueError:
        mmop = True
    if ord(vvc[0]) << 1 != num:
        mmop = True
    if mmop:
        return 'Key check failed on the third segment'
    return None


def ppap(vvc):

    if len(vvc) != 17:
        return 'Invalid key format'

    if vvc[5] != '-' or vvc[11] != '-':
        return 'Invalid key format'

    error = gfew(vvc[:5])
    if error:
        return error
    error = gfaw(vvc)
    if error:
        return error
    error = gfaf(vvc)
    if error:
        return error
    return None


def main():
    error = None
    value = None
    messagebox.showinfo('Info', 'AllahGuardSerialChecker will now check for a serial key.'
                                'Please donate to our open source project!')
    try:
        # I'm not sure where on the system we expect the key to be saved. 
        # We might go back to an idea I had in the past.
        # key = get_key()
        pass
    except FileNotFoundError:
        error = 'Serial key not found'
    if not error:
        error = ppap(key)
    if error:
        # Hide the root TK window
        root = tk.Tk()
        root.withdraw()

        # Show a message box with the error using tkinter
        messagebox.showerror('Error', error)
        exit(-1)


if __name__ == '__main__':
    main()
