echo "Enter 2 numbers: "
read a
read b

if [ $a -gt $b ]
then
	echo "$a is the biggest"
elif [ $b -gt $a ]
then
	echo "$b is the biggest"
else
	echo "The numbers are equal"
fi
