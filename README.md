[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19318224.svg)](https://doi.org/10.5281/zenodo.19318224)
![Ubuntu](https://img.shields.io/badge/Platform-Ubuntu-orange)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Stable-success)

# NordVPN Toggle for Ubuntu

A lightweight GUI and CLI utility to enable or disable system-wide NordVPN on Ubuntu.

## Features
- One-click GUI VPN toggle (Tkinter-based)
- Command-line toggle script
- System-wide VPN control via NordVPN CLI
- Ideal for cybersecurity research and teaching

## Installation

Install NordVPN:
sh <(curl -sSf https://downloads.nordcdn.com/apps/linux/install.sh)

Login and configure:
nordvpn login
sudo usermod -aG nordvpn $USER
reboot

Run GUI:
python3 nordvpn_toggle.py

Run CLI:
./nordvpn-toggle.sh

## Author
Mohit Tiwari  
Assistant Professor, CSE  
Bharati Vidyapeeth's College of Engineering, New Delhi  
ORCID: 0000-0003-1836-3451
