#!/bin/bash
USED_PERCENT=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
FREE_PERCENT=$((100 - USED_PERCENT))
echo "Notifikasi: Space HDD anda tinggal $FREE_PERCENT%"
