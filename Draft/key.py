#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import win32gui
import win32con
import time
import pyautogui
app_dir = r'C:\Program Files (x86)\Infineon\Memtool 4.7\IMTMemtool.exe'
# def open_app(app_dir):
pyautogui.FAILSAFE = False
os.startfile(app_dir)
time.sleep(1)
# if __name__ == "__main__":
#   open_app(app_dir)
# pyautogui.moveTo(-714, 724, duration=1)
# pyautogui.click()
# handle = win32gui.FindWindow("tooltips_class32", "Infineon - Memtool on TriBoard with TC233/TC234/TC237 (DAS)")

handle = win32gui.FindWindow(None,"Infineon - Memtool on TriBoard with TC233/TC234/TC237 (DAS)")
# handle = win32gui.FindWindow(None,app_dir)
hwnd = "Infineon - Memtool on TriBoard with TC233/TC234/TC237 (DAS)"
rect = win32gui.GetWindowRect(handle)
x = rect[0]
y = rect[1]
w = rect[2] - x
h = rect[3] - y
print("Window %s:" % win32gui.GetWindowText(handle))
print("\tLocation: (%d, %d)" % (x, y))
print("\t    Size: (%d, %d)" % (w, h))
win32gui.SetWindowPos(handle, win32con.HWND_TOPMOST, 0,0,w,h, win32con.SWP_SHOWWINDOW)
# pyautogui.moveTo(0,0,1)
#select 8K
pyautogui.click(938,117,1, 0.0, 'left')
time.sleep(1)
pyautogui.click(635,168,1, 0.0, 'left')
time.sleep(1)
# connect

#点击connect
pyautogui.click(368,466,1, 0.0, 'left')
time.sleep(3)
#open file
pyautogui.click(373,165,1, 0.0, 'left')
time.sleep(1)
handle1 = win32gui.FindWindow(None,"Open Hex File")
rect1 = win32gui.GetWindowRect(handle)
x1 = rect[0]
y1 = rect[1]
w1 = rect[2] - x
h1= rect[3] - y

win32gui.SetWindowPos(handle1, win32con.HWND_TOPMOST, 0,0,1029,461, win32con.SWP_SHOWWINDOW)

pyautogui.click(630,61,1, 0.0, 'left')
time.sleep(1)
pyautogui.press('shift')
pyautogui.write('C:\Sandbox\SGM458\Project_Information\Releases\PR3062', interval=0.01)
pyautogui.click(736,70,1, 0.0, 'left')
time.sleep(2)
# all files
pyautogui.click(914,390,1, 0.0, 'left')
time.sleep(1)
pyautogui.click(837,461,1, 0.0, 'left')
time.sleep(1)



#search disable
pyautogui.click(876,59,2, 0.0, 'left')
time.sleep(1)
pyautogui.write('disable', interval=0.01)
pyautogui.press('shift')
pyautogui.press('enter')
time.sleep(2)
# select disable
pyautogui.click(635,153,2, 0.0, 'left')
time.sleep(5)
pyautogui.click(161,159,1, 0.0, 'left')
time.sleep(2)
# add select
pyautogui.click(358,238,1, 0.0, 'left')
time.sleep(2)
#progtam
pyautogui.click(1029,200,1, 0.0, 'left')
time.sleep(3)
# exit
pyautogui.click(546,431,1, 0.0, 'left')
time.sleep(1)
#disconnected
pyautogui.click(368,466,1, 0.0, 'left')
time.sleep(2)

#select 2M
pyautogui.click(938,117,1, 0.0, 'left')
time.sleep(1)
pyautogui.click(637,141,1, 0.0, 'left')
time.sleep(1)
#connect
pyautogui.click(368,466,1, 0.0, 'left')
time.sleep(3)
#erase
pyautogui.click(1018,167,1, 0.0, 'left')
time.sleep(1)
#erase select
pyautogui.click(321,157,1, 0.0, 'left')
time.sleep(2)
# Erase 6
pyautogui.click(343,345,1, 0.0, 'left')
time.sleep(2)
#select
pyautogui.click(663,375,9, 0.0, 'left')
time.sleep(1)
# erase 16
pyautogui.click(344,361,1, 0.0, 'left')
time.sleep(1)
# start
pyautogui.click(743,130,1, 0.0, 'left')
time.sleep(2)
# exit
pyautogui.click(548,423,1, 0.0, 'left')
time.sleep(2)
# disconnect
pyautogui.click(371,472,1, 0.0, 'left')
time.sleep(1)
# seclect 8K
pyautogui.click(938,117,1, 0.0, 'left')
time.sleep(1)
pyautogui.click(589,168,1, 0.0, 'left')
time.sleep(1)
# connected
pyautogui.click(368,466,1, 0.0, 'left')
time.sleep(2)
#open file
pyautogui.click(373,165,1, 0.0, 'left')
time.sleep(1)

#search enable
pyautogui.click(918,61,1, 0.0, 'left')
time.sleep(1)
pyautogui.write('enable', interval=0.1)
pyautogui.press('enter')
# select enable
pyautogui.click(572,153,2, 0.0, 'left')
time.sleep(2)
pyautogui.click(163,162,1, 0.0, 'left')
time.sleep(1)

# add select
pyautogui.click(358,238,1, 0.0, 'left')
time.sleep(2)
#progtam
pyautogui.click(1029,200,1, 0.0, 'left')
time.sleep(2)
# exit
pyautogui.click(546,431,1, 0.0, 'left')
time.sleep(1)

pyautogui.click(1030,465,1, 0.0, 'left')
time.sleep(1)
# bhandle = win32gui.FindWindowEx(handle, 0, "Button", "Connect")
# win32gui.PostMessage(bhandle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
# win32gui.PostMessage(bhandle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)
# time.sleep(5)
#
# bhandle1 = win32gui.FindWindowEx(handle, 0, "Button", "Open Hex File")
# win32gui.PostMessage(bhandle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
# win32gui.PostMessage(bhandle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)
# print(bhandle1)
# bhandle2 = win32gui.FindWindowEx(handle, 0, "Button", "HSMCOTP_boot_disable.hex")
# win32gui.PostMessage(bhandle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
# win32gui.PostMessage(bhandle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)
# bhandle3 = win32gui.FindWindowEx(handle, 0, "Button", "HSMCOTP_boot_disable.hex")
# win32gui.PostMessage(bhandle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
# win32gui.PostMessage(bhandle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)