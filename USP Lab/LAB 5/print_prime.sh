echo "Enter m and n:"
read m
read n
while [ $m -le $n ]
do
	i=2
	flag=0
	while test $i -le `expr $m / 2`
	do
		if test `expr $m % $i` -eq 0
		then
			flag=1
		fi

	i=`expr $i + 1`
	done 

	if test $flag -ne 1
	then
		if test $m -ne 1
		then
			printf "$m "
		fi
	fi
	m=$((m+1))
  
done
echo ""
