#!/bin/sh

mknod /dev/mmcblk0p1 b 179 1
mount -o ro /dev/mmcblk0p1 /boot

if [ -f "/boot/keybow" ]; then
	cp /boot/keybow /usr/bin/keybow
	chmod +x /usr/bin/keybow
fi

/usr/bin/keybow