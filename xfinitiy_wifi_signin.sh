#!/bin/bash
nmcli radio wifi off
sudo macchanger -r wlp2s0
nmcli radio wifi on
echo "waiting.."
while ! ifconfig wlp2s0 | grep 'inet '; do
	sleep 1
done
python3 ./xfinity_wifi_signin.py
