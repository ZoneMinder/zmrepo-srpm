#!/bin/bash

ID="/usr/bin/id"

if [ "$($ID -u)" -eq 0 ]; then
    echo
    echo "ERROR: This script must NOT be run as root. Aborting..."
    echo
    exit 1
fi

# Verify the script was passed an arugement
if [ ! -f "$1" ]; then
    echo
    echo "ERROR: This script requires the full path to a zoneminder RPM source file."
    echo "A valid RPM source file was not detected from the given command line argument."
    echo
    exit 1
fi

# armv7hl
mock -r zmrepo-f21-armhfp --clean
mock -r zmrepo-f21-armhfp --init
#mock -r zmrepo-f21-armhfp --copyin /home/abauer/rpmbuild/SPECS/ln_ffmpeg.sh /root/
#mock -r zmrepo-f21-armhfp --shell /root/ln_ffmpeg.sh
mock -r zmrepo-f21-armhfp --shell for FOLDER in libavcodec libavdevice libavfilter libavformat libavresample libavutil libpostproc libswresample libswscale; do ln -sf /usr/include/ffmpeg/$FOLDER/ /usr/include/$FOLDER; done
mock -r zmrepo-f21-armhfp --no-clean $1

echo
echo "If the build was successful, RPMs should be listed below"
echo
ls /var/lib/mock/fedora-21-armhfp/result/*.rpm

