#!/usr/bin/sh

PANEL_FIFO=/tmp/panel-fifo

amixer set Master 5%+ > /dev/null 

echo "V$(amixer sget Master | tail -n 1 | awk '{print $4}' | tr -d "[]")" > "$PANEL_FIFO" &
