#!/bin/bash
STATUS=$(nordvpn status | grep "Status")

if [[ $STATUS == *"Connected"* ]]; then
    nordvpn disconnect
    notify-send "NordVPN Toggle" "VPN Disconnected"
else
    nordvpn connect
    notify-send "NordVPN Toggle" "VPN Connected"
fi
