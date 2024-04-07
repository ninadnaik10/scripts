#!/bin/bash

# Start bluetoothctl
bluetoothctl << EOF
menu gatt
register-service 0000110d-0000-1000-8000-00805f9b34fb
yes
quit
EOF

# Restart the Bluetooth service
sudo systemctl restart bluetooth
sleep 5
bluetoothctl << EOF
connect E4:41:22:FC:FB:DC
quit
EOF

# Enter Device Address above
