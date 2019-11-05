#!/bin/bash

coproc bluetoothctl
echo -e 'info E6:51:A6:1A:37:5B\nexit' >&${COPROC[1]}
output=$(cat <&${COPROC[0]})
echo $output