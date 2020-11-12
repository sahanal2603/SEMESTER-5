printf "Enter number: "
read n
printf "Enter power: "
read p

counter=0
ans=1

while [ $p -ne $counter ]
do
        ans=`expr $ans \* $n`
        counter=`expr $counter + 1`
done

echo "$n to the power $p is $ans"
