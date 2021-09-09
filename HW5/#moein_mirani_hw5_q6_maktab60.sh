#! bin/usr/bash
read directory
cd $directory
touch results.txt
for i in `$directory | ls -F`
do
	if [[ ${i:(-1)} != "/" ]]
	then
		cat "$i" >> results.txt
	fi
done
sort results.txt | head -10 | tail -5

