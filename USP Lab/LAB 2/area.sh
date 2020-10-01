echo "Enter length and breadth"
read l
read b
arectangle=$(echo "$l * $b" | bc)
printf "Area of Rectangle: "$arectangle
echo "\n"
prectangle=$(echo "2 * ($l + $b)" | bc)
printf "Perimeter of Rectangle: "$prectangle
echo "\n"

echo "Enter breadth and height of triangle"
read br
read h
atriangle=$(echo "0.5 * $br * $h" | bc)
printf "Area of Triangle: "$atriangle
echo "\n"

echo "Enter radius of circle"
read r
acircle=$(echo "3.14 * $r * $r" | bc)
echo "Area of Circle: "$acircle
pcircle=$(echo "2 * 3.14 * $r" | bc)
echo "Perimeter of Circle: "$pcircle
echo "\n"

echo "Enter side of square"
read a
asquare=$(echo "$a * $a" | bc)
printf "Area of square: "$asquare
psquare=$(echo "4 * $a" | bc)
echo "\n"
printf "Perimeter of square: "$psquare
echo "\n"
