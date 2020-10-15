echo "ENTER 2 NUMBERS"
read a
read b

echo "\nMENU \n1.ADDITION \n2.SUBTRACTION \n3.MULTIPLICATION \n4.DIVISION \n5.MODULUS \nENTER YOUR CHOICE:\c"
read choice

case "$choice" in
	1) printf "SUM: "; expr $a + $b ;;
	2) printf "DIFFERENCE: "; expr $a - $b ;;
	3) printf "PRODUCT: "; expr $a \* $b ;;
	4) printf "QUOTIENT: "; expr $a / $b ;;
	5) printf "REMAINDER: "; expr $a % $b ;;
	*) echo "INVALID CHOICE" ;;
esac
