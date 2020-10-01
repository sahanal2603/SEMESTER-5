echo "enter values of 2 operands"
read a
read b
printf "Addition: "
expr $a + $b
printf "Subtraction: "
expr $a - $b
printf "Multiplication: "
expr $a \* $b
printf "Division: "
expr $a / $b
printf "Modulus: "
expr $a % $b
