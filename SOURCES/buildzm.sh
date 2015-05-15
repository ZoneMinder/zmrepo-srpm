#!/bin/bash
# This script assists the end user with building a zoneminder rpm
# All work is done in a chroot environment using mock

usage()
{
cat <<EOF
USAGE: $0 MOCKCONFIG SRPM

MOCKCONFIG is the name of a mock configuration file found under /etc/mock.
SRPM is the full path to a valid zoneminder source rpm

This script cannot be run as root and can only be run by a user who is a
member of the group mock.

EXAMPLE:
buildzm.sh zmrepo-f21-x86_64 ~/rpmbuild/SRPMS/zoneminder-1.28.1master-1.fc21.src.rpm

EOF
}

# Define the executables used by this script
ID="/usr/bin/id"
MOCK="/usr/bin/mock"

#
# Begin Sanity Checks
#

# We don't want to run as root
if [ "$($ID -u)" -eq 0 ]; then
    echo
    echo "ERROR: This script must NOT be run as root. Aborting..."
    echo
    exit 1
fi

# Verify the user passed two arguments to the script
if [ "$#" -ne 2 ]; then 
    echo
    echo "ERROR: This script requires two commandline arguments."
    echo
    usage
    exit 0
fi

# Verify the first argument points to an existing mock configuration file
if [ ! -f "/etc/mock/$1.cfg" ]; then
    echo
    echo "ERROR: This script requires the user to specify a valid mock configuration file."
    echo "A valid mock configuration file was not detected from the given command line argument."
    echo
    usage
    exit 1
fi

# Verify the second argument points to an existing source rpm.
if [ ! -f "$2" ] && [[ "$2" != *".src.rpm" ]]; then
    echo
    echo "ERROR: This script requires the full path to a zoneminder RPM source file."
    echo "A valid RPM source file was not detected from the given command line argument."
    echo
    usage
    exit 1
fi

#
# Sanity Checks Complete. Now on to doing the actual work.
#

$MOCK -r $1 --clean
$MOCK -r $1 --init
$MOCK -r $1 --shell "sh -c 'for FOLDER in libavcodec libavdevice libavfilter libavformat libavresample libavutil libpostproc libswresample libswscale; do ln -sf /usr/include/ffmpeg/$FOLDER/ /usr/include/$FOLDER; done'"
$MOCK -r $1 --no-clean $2

if [ "$?" -eq 0  ]; then
	echo
	echo "The build script reported success. RPMs should be listed below..."
	echo
	ls /var/lib/mock/$1/result/*.rpm 2> /dev/null
else
	echo
	echo "The build script reported failure. You should inspect the build logfiles..."
	echo
	ls /var/lib/mock/$1/result/*.log 2> /dev/null
fi


