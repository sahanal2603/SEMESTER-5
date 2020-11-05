printf "Enter a number: "
read num

x=1
sum=0

while [ $x -le $num ]
do
	sum=$((sum + $x))
	x=$((x+1))
  
done

echo "Sum of first $num natural numbers is $sum"
