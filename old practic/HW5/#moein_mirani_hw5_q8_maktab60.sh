#! bin/usr/sh
read directory1
read directory2
cd $directory1
for i in `ls $directory1`
do
	if [[ $i =~ "a" ]] &&  [ "$(file $i)" = "$i: ASCII text" ]
	then
		cp $i $directory2
	fi
done


