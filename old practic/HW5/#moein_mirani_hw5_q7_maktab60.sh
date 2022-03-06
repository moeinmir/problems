#! bin/usr/bash
read directory
if [ -d $directory ]
then
	echo the directory exist
else
	mkdir $directory
fi
