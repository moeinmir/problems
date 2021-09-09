#! bin/usr/bash
number_of_files=0
number_of_folders=0
read directory
for i in `$directory | ls -F`
do
	if [[ ${i:(-1)} = "/" ]]
	then
		$((number_of_folders=number_of_folders+1))
	else
		$((number_of_files=number_of_files+1))
	fi
done
echo number of files: $number_of_files
echo number of folders: $number_of_folders


