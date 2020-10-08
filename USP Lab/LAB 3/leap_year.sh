echo "enter year: "
read y

leap=0

if [ $(expr $y % 4) = 0 ] && [ $(expr $y % 100) != 0 ] 
then 
	leap=1
elif [	$(expr $y % 100) = 0 ] && [ $(expr $y % 400) = 0 ]
then 
	leap=1
else
	leap=0
fi


if [ $leap = 1 ]
then
	echo "Leap year"
else	
	echo "Not a leap year"
fi
