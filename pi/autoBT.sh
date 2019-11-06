#!/bin/bash

sudo hciconfig hci0 down
sudo hciconfig hci0 up

coproc bluetoothctl
echo -e 'remove E6:51:A6:1A:37:5B\nconnect E6:51:A6:1A:37:5B\npair E6:51:A6:1A:37:5B\nexit' >&${COPROC[1]}
output=$(cat <&${COPROC[0]})
echo $output