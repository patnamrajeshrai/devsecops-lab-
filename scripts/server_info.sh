#!/bin/bash

echo "===== Server Information ====="
echo "Hostname: $(hostname)"
echo "Operating System:"
. /etc/os-release
echo "$PRETTY_NAME"
echo "Kernel: $(uname -r)"
echo "CPU cores: $(nproc)"
echo "Memory:"
free -h
echo "Disk:"
df -h /
