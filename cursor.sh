#!/bin/bash
if [ "$1" = "." ]; then
    cursor_path=$(find /home/${USER}/Applications -name "cursor-*.AppImage" | head -n 1)
    "$cursor_path" "$(pwd)" &>/dev/null & disown
else
    cursor_path=$(find /home/${USER}/Applications -name "cursor-*.AppImage" | head -n 1)
    "$cursor_path" "$@" &>/dev/null & disown
fi
