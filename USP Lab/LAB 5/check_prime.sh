printf "Enter a number: "
read number
i=2
flag=0

while test $i -le `expr $number / 2`
do
	if test `expr $number % $i` -eq 0
	then
		flag=1
	fi

	i=`expr $i + 1`
done 

if test $flag -eq 1
then
	echo "$number number is Not a Prime number"
else
	echo "$number number is a Prime number"
fi
