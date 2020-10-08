echo "Enter 3 numbers: "
read a
read b
read c

if [ $a -gt $b ]
then
	if [ $a -gt $c ]
	then 
		echo "$a is the biggest number"
	else
		echo "$c is the biggest number"
	fi
elif [ $b -gt $c ]
then
	echo "$b is the biggest number"
else 
	echo "$c is the biggest number"
fi
