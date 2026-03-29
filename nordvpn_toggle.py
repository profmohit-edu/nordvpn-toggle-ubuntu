#!/usr/bin/env python3
import subprocess
import tkinter as tk

def run_command(command):
    return subprocess.getoutput(command)

def get_status():
    status_output = run_command("nordvpn status")
    return "Connected" if "Connected" in status_output else "Disconnected"

def toggle_vpn():
    status = get_status()
    if status == "Connected":
        run_command("nordvpn disconnect")
        status_label.config(text="VPN Disconnected", fg="red")
        toggle_button.config(text="Connect VPN")
    else:
        run_command("nordvpn connect")
        status_label.config(text="VPN Connected", fg="green")
        toggle_button.config(text="Disconnect VPN")

def refresh_status():
    status = get_status()
    if status == "Connected":
        status_label.config(text="VPN Connected", fg="green")
        toggle_button.config(text="Disconnect VPN")
    else:
        status_label.config(text="VPN Disconnected", fg="red")
        toggle_button.config(text="Connect VPN")

root = tk.Tk()
root.title("NordVPN Toggle - Ubuntu")
root.geometry("320x180")
root.resizable(False, False)

title = tk.Label(root, text="NordVPN System-Wide Toggle", font=("Arial", 12, "bold"))
title.pack(pady=10)

status_label = tk.Label(root, text="Checking...", font=("Arial", 11))
status_label.pack(pady=5)

toggle_button = tk.Button(root, text="Toggle VPN", command=toggle_vpn, width=20)
toggle_button.pack(pady=10)

refresh_button = tk.Button(root, text="Refresh Status", command=refresh_status, width=20)
refresh_button.pack(pady=5)

refresh_status()
root.mainloop()
