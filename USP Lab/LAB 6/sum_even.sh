printf "Enter a number: "
read n

x=2
sum=0

while [ $x -le $n ]
do
	if [ $(expr $x % 2) = 0 ] 
	then
		sum=$((sum + $x))
	fi
	x=$((x+1))
  
done

echo "Sum of even numbers upto $n is $sum"
