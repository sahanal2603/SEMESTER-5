echo "ENTER STUDENT MARKS IN 3 SUBJECTS: "
read s1
read s2
read s3

total=$(echo "$s1 + $s2 + $s3" | bc)
printf "\nTOTAL MARKS: "$total


avg=$(echo "$total / 3" | bc)
printf "\nAVERAGE: "$avg


if [ $avg -ge 90 ] && [ $avg -le 100 ]
then
	echo "\nDISTINCTION"
elif [ $avg -ge 65 ] && [ $avg -lt 90 ]
then 
	echo "\nFIRST CLASS"
elif [ $avg -ge 40 ] && [ $avg -lt 65 ]
then 
	echo "\nSECOND CLASS"
	
else
	echo "\nFAIL"
fi



