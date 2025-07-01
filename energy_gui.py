import serial
import tkinter as tk

ser = serial.Serial('COM3', 9600)

root = tk.Tk()
root.title("Smart Energy Meter")

voltage_var = tk.StringVar()
current_var = tk.StringVar()
power_var = tk.StringVar()

tk.Label(root, text="Voltage (V):").grid(row=0, column=0)
tk.Label(root, textvariable=voltage_var).grid(row=0, column=1)

tk.Label(root, text="Current (A):").grid(row=1, column=0)
tk.Label(root, textvariable=current_var).grid(row=1, column=1)

tk.Label(root, text="Power (W):").grid(row=2, column=0)
tk.Label(root, textvariable=power_var).grid(row=2, column=1)

def update_values():
    try:
        line = ser.readline().decode('utf-8').strip()
        voltage, current, power = line.split(',')
        voltage_var.set(voltage)
        current_var.set(current)
        power_var.set(power)
    except:
        voltage_var.set("Error")
        current_var.set("Error")
        power_var.set("Error")
    root.after(1000, update_values)

update_values()
root.mainloop()
