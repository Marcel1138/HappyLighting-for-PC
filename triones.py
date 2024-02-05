#!/usr/bin/python3
import sys
import tkinter as tk
from tkinter import ttk, colorchooser
import trionesControl.trionesControl as tc

WARM_WHITE = "ffd700" 
COOL_WHITE = "00bfff"  

def set_color():
    chosen_color = colorchooser.askcolor()[1]
    if chosen_color:
        hex_color = chosen_color[1:]
        set_led_color(hex_color)

def set_warm_white():
    set_led_color(WARM_WHITE)

def set_cool_white():
    set_led_color(COOL_WHITE)

def set_led_color(hex_color):
    print("Setting color to #" + hex_color)

    col_rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    R, G, B = col_rgb

    tc.powerOn(device)
    tc.setRGB(R, G, B, device)

def turn_off_led():
    print("Turning off the light")
    tc.powerOff(device)

def turn_on_led():
    print("Turning on the light")
    tc.powerOn(device)

def on_exit():
    tc.disconnect(device)
    root.destroy()

if __name__ == "__main__":
    # Connect to the LED 
    device = tc.connect('YOUR MAC HERE!!') # Use  "$ sudo hcitool lescan" to find the Mac

    # GUI 
    root = tk.Tk()
    root.title("LED Controller")

    style = ttk.Style()
    style.configure("TButton", padding=10, font=('Helvetica', 12))

    frame = ttk.Frame(root, padding="20")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    color_button = ttk.Button(frame, text="Choose Color", command=set_color)
    color_button.grid(row=0, column=0, padx=10, pady=10)

    warm_white_button = ttk.Button(frame, text="Warm White", command=set_warm_white)
    warm_white_button.grid(row=0, column=1, padx=10, pady=10)

    cool_white_button = ttk.Button(frame, text="Cool White", command=set_cool_white)
    cool_white_button.grid(row=1, column=0, padx=10, pady=10)

    turn_on_button = ttk.Button(frame, text="Turn On", command=turn_on_led)
    turn_on_button.grid(row=1, column=1, padx=10, pady=10)

    turn_off_button = ttk.Button(frame, text="Turn Off", command=turn_off_led)
    turn_off_button.grid(row=2, column=0, columnspan=2, pady=10)

    exit_button = ttk.Button(frame, text="Exit", command=on_exit)
    exit_button.grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()
