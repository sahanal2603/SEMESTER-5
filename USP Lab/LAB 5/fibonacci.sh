c=2
a=1
b=1
d=0
printf "Enter number of elements: "
read n
echo "$a"
echo "$b"
while [ $c -lt $n ] 
do
	d=$((a+b))
	echo "$d"
	a=$b
	b=$d
	c=$((c+1))
done

